#include <iostream>
#include <fstream>
#include <sys/stat.h>
#include <ctime>
#include <stdlib.h>
using namespace std;

typedef unsigned char uc;
static const unsigned short crc16tab[256]= {        // poly = 0x11021
 0x0000,0x1021,0x2042,0x3063,0x4084,0x50a5,0x60c6,0x70e7,
 0x8108,0x9129,0xa14a,0xb16b,0xc18c,0xd1ad,0xe1ce,0xf1ef,
 0x1231,0x0210,0x3273,0x2252,0x52b5,0x4294,0x72f7,0x62d6,
 0x9339,0x8318,0xb37b,0xa35a,0xd3bd,0xc39c,0xf3ff,0xe3de,
 0x2462,0x3443,0x0420,0x1401,0x64e6,0x74c7,0x44a4,0x5485,
 0xa56a,0xb54b,0x8528,0x9509,0xe5ee,0xf5cf,0xc5ac,0xd58d,
 0x3653,0x2672,0x1611,0x0630,0x76d7,0x66f6,0x5695,0x46b4,
 0xb75b,0xa77a,0x9719,0x8738,0xf7df,0xe7fe,0xd79d,0xc7bc,
 0x48c4,0x58e5,0x6886,0x78a7,0x0840,0x1861,0x2802,0x3823,
 0xc9cc,0xd9ed,0xe98e,0xf9af,0x8948,0x9969,0xa90a,0xb92b,
 0x5af5,0x4ad4,0x7ab7,0x6a96,0x1a71,0x0a50,0x3a33,0x2a12,
 0xdbfd,0xcbdc,0xfbbf,0xeb9e,0x9b79,0x8b58,0xbb3b,0xab1a,
 0x6ca6,0x7c87,0x4ce4,0x5cc5,0x2c22,0x3c03,0x0c60,0x1c41,
 0xedae,0xfd8f,0xcdec,0xddcd,0xad2a,0xbd0b,0x8d68,0x9d49,
 0x7e97,0x6eb6,0x5ed5,0x4ef4,0x3e13,0x2e32,0x1e51,0x0e70,
 0xff9f,0xefbe,0xdfdd,0xcffc,0xbf1b,0xaf3a,0x9f59,0x8f78,
 0x9188,0x81a9,0xb1ca,0xa1eb,0xd10c,0xc12d,0xf14e,0xe16f,
 0x1080,0x00a1,0x30c2,0x20e3,0x5004,0x4025,0x7046,0x6067,
 0x83b9,0x9398,0xa3fb,0xb3da,0xc33d,0xd31c,0xe37f,0xf35e,
 0x02b1,0x1290,0x22f3,0x32d2,0x4235,0x5214,0x6277,0x7256,
 0xb5ea,0xa5cb,0x95a8,0x8589,0xf56e,0xe54f,0xd52c,0xc50d,
 0x34e2,0x24c3,0x14a0,0x0481,0x7466,0x6447,0x5424,0x4405,
 0xa7db,0xb7fa,0x8799,0x97b8,0xe75f,0xf77e,0xc71d,0xd73c,
 0x26d3,0x36f2,0x0691,0x16b0,0x6657,0x7676,0x4615,0x5634,
 0xd94c,0xc96d,0xf90e,0xe92f,0x99c8,0x89e9,0xb98a,0xa9ab,
 0x5844,0x4865,0x7806,0x6827,0x18c0,0x08e1,0x3882,0x28a3,
 0xcb7d,0xdb5c,0xeb3f,0xfb1e,0x8bf9,0x9bd8,0xabbb,0xbb9a,
 0x4a75,0x5a54,0x6a37,0x7a16,0x0af1,0x1ad0,0x2ab3,0x3a92,
 0xfd2e,0xed0f,0xdd6c,0xcd4d,0xbdaa,0xad8b,0x9de8,0x8dc9,
 0x7c26,0x6c07,0x5c64,0x4c45,0x3ca2,0x2c83,0x1ce0,0x0cc1,
 0xef1f,0xff3e,0xcf5d,0xdf7c,0xaf9b,0xbfba,0x8fd9,0x9ff8,
 0x6e17,0x7e36,0x4e55,0x5e74,0x2e93,0x3eb2,0x0ed1,0x1ef0
};

string strxchar(string raw_, int len_, char fill_='0', bool forward_=true){
    int cx;
    string cooked = raw_;
    for(cx=0; cx<len_-raw_.size(); cx++)
        cooked = forward_? fill_ + cooked: cooked + fill_;
    return cooked;
}

int main()
{
    std::cout << "======== ======== ======== ========\n";
    std::cout << "======== BinPackage 3.0 mx ========\n";
    std::cout << "======== ======== ======== ========\n"; 
//============= load setting ================
    struct _stat stf_info, src_info, dst_dir_info;
    string line[3];
    fstream stf;
    string stf_name = "bin_package_setting.txt";
    if((_stat(stf_name.data(), &stf_info) == 0) &&(stf_info.st_mode &S_IFREG))
        cout << "Successfully open setting file." <<endl;
    else{
        cout << "Setting file missed, reset." <<endl;
        stf.open(stf_name, ios::out);
        stf << "/* first line is last source file, second line is output directory.\
                (don't miss the '/' at the end of directory.)*/" <<endl;
        stf << "none" <<endl;
        stf << "./";
        stf.close();
    }
    stf.open(stf_name, ios::in);
    getline(stf, line[0]);  getline(stf, line[1]);
    getline(stf, line[2]);
    stf.close();
    if((_stat(line[1].data(), &src_info) == 0) &&(src_info.st_mode &S_IFREG))
        cout << "Last source file: " << line[1] <<endl;
    else{
        cout << "!!! Last source file can not found, reset." <<endl;
        line[1] = "none";
    }
    
    if((_stat(line[2].data(), &dst_dir_info) == 0) &&(dst_dir_info.st_mode &S_IFDIR))
        cout << "Output directory: " << line[2] <<endl;
    else{
        cout << "!!! Invalid output directory, reset." <<endl;
        line[2] = "./";
    }
    cout <<endl;
//============= get input file ===============
    string in_filename;
    string pre_filename = line[1];
    struct _stat f_info;
    for(;;){
        string scan_str;
        cout << "Input file (enter to load last source file) >>>";
        getline(cin, scan_str);
        if(scan_str == "")
            scan_str = pre_filename;
        if((_stat(scan_str.data(), &f_info) == 0) &&(f_info.st_mode &S_IFREG)){
            in_filename = scan_str;
            break;
        }
        else
            cout << "!!! The file do not exist anymore. try again, pls." <<endl;
    }
    cout << "Get input file : " << in_filename <<endl;
    cout << "----Last modified at " << ctime(&(f_info.st_mtime)) <<endl;

    stf.open(stf_name, ios::out);
    stf << line[0] <<endl;
    stf << in_filename <<endl;
    stf << line[2];
    stf.close();

//================= header =================
    char header[2] = {(char)0xc5, (char)0x84};

//============= get data length ==========
    ifstream fi(in_filename, ifstream::binary);
    unsigned data_length, data_length_bit;
    char data_length_3B[3];
    data_length = f_info.st_size;
    cout << "Data length : " << data_length << " B" <<endl;
    data_length_bit = data_length *8;
    data_length_3B[0] = (uc)((data_length_bit >>16) &0x00ff);
    data_length_3B[1] = (uc)((data_length_bit >> 8) &0x00ff);
    data_length_3B[2] = (uc)((data_length_bit     ) &0x00ff);

//============= get current time ============
    time_t now = time(0);
    tm *our_tm = localtime(&now);
    char tm_6B[6];
    cout << "Packing time: ";
    cout << (our_tm->tm_year - 100) << '-' << (our_tm->tm_mon + 1) << '-' << our_tm->tm_mday << ' ';
    cout << our_tm->tm_hour << ':' << our_tm->tm_min << ':' << our_tm->tm_sec <<endl;
    tm_6B[0] = (uc)(our_tm->tm_year - 100);
    tm_6B[1] = (uc)(our_tm->tm_mon + 1);
    tm_6B[2] = (uc)(our_tm->tm_mday);
    tm_6B[3] = (uc)(our_tm->tm_hour);
    tm_6B[4] = (uc)(our_tm->tm_min );
    tm_6B[5] = (uc)(our_tm->tm_sec );

    // genetate output filename and get path
    string out_filename = line[2] + "pkg--"
                        + strxchar(to_string(our_tm->tm_mon + 1), 2)
                        + strxchar(to_string(our_tm->tm_mday),    2)+ "--"
                        + strxchar(to_string(our_tm->tm_hour),    2) + '_'
                        + strxchar(to_string(our_tm->tm_min ),    2) + '_'
                        + strxchar(to_string(our_tm->tm_sec ),    2) + ".bin";
    cout  << "Output file : " << out_filename << endl;

    ofstream fo(out_filename, ofstream::binary);
    // output begin
    fo.write(header, 2);
    fo.write(data_length_3B, 3);
    fo.write(tm_6B + 3 , 3);

//============= get crc ==================
    fi.seekg(0, ios::beg);
    char data;
    unsigned short int_data, crc = 0;
    while(fi.read(&data, sizeof(data))){
        int_data = (int)(uc)data;
        crc = (crc << 8) ^crc16tab[((crc >> 8) ^int_data) &0x00ff];
        fo.write(&data, 1);
    }
    fi.close();
    cout.flags(ios::hex |ios::showbase);
    // cout << "CRC = " << crc <<endl;
    char crcHB = (uc)((crc >>8) &0x00ff);
    char crcLB = (uc)((crc    ) &0x00ff);
    fo.write(&crcHB, 1);
    fo.write(&crcLB, 1);

//============= supple 0 ====================
    char zero = 0;
    int zp;
    for(zp=0; zp<(data_length+10)%4; zp++)
        fo.write(&zero, 1);
    fo.close();

    cout << "\n\n[P.S.] You can set output directory in setting file." <<endl;
    system("pause");
    return 0;
}

