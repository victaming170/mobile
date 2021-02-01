#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <sys/stat.h>

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
int main(){
    printf("======== ======== ======== ========\n");
    printf("======== BinPackage 3.0 mx ========\n");
    printf("======== ======== ======== ========\n"); 
//======================== load config ========================
    FILE *f_cfg;
    struct _stat cfg_info;
    char cfg_comment[160], cfg_src[128], cfg_out[128];
    char *cfg_name = "bin_package.cfg";

    // check config existing
    if((_stat(cfg_name, &cfg_info) == 0) &&(cfg_info.st_mode &S_IFREG))
        printf("Successfully open config file.\n");
    else{
        printf("Setting file missed, reset.\n");
        f_cfg = fopen(cfg_name, "w");
        fputs("/* first line is last source file, second line is output directory.*/\n", f_cfg);
        fputs("none\n", f_cfg);
        fputs("./", f_cfg);
        fclose(f_cfg);
    }

    // get last source file, and output directory
    f_cfg = fopen(cfg_name, "r");
    fgets(cfg_comment, 160, f_cfg);
    fgets(cfg_src   , 128, f_cfg);
    fgets(cfg_out   , 128, f_cfg);
    fclose(f_cfg);

    char src_name[128], outdir_name[128];
    strcpy(src_name, cfg_src);
    src_name[strlen(cfg_src) - 1] = '\0';
    if(cfg_out[strlen(cfg_out)-1] == '\n'){
        strcpy(outdir_name, cfg_out);
        outdir_name[strlen(cfg_out)-1] = '\0';
    }
    else
        strcpy(outdir_name, cfg_out);
    // printf("%s", cfg_comment); printf("%s", cfg_src); printf("%s\n", cfg_out);

    struct _stat src_info;
    if((_stat(src_name, &src_info) == 0) &&(src_info.st_mode &S_IFREG))
        printf("Last source file: %s\n", src_name);
    else{
        printf("!!! Last source file can not found, reset.\n");
        strcpy(cfg_src, "none\n");
    }

    struct _stat out_info;
    if((_stat(outdir_name, &out_info) == 0) &&(out_info.st_mode &_S_IFDIR))
        printf("Output directory: %s\n", outdir_name);
    else{
        printf("!!! Invalid output directory, reset.\n");
        strcpy(outdir_name, "./");
    }

    printf("\n");   // block end
//======================== get input file, and dump to config ========================
    char in_filename[128];
    struct _stat fin_info;
    while(1){
        char scan_str[128];
        printf("Input file (enter to load last source file) >>>");
        gets(scan_str);
        if(strlen(scan_str) == 0)
            strcpy(scan_str, src_name);
        if((_stat(scan_str, &fin_info) == 0) &&(fin_info.st_mode &S_IFREG)){
            strcpy(in_filename, scan_str);
            break;
        }
        else
            printf("!!! The file doesn't exist. Try again, pls.\n");
    }
    printf("Get input file : %s\n", in_filename);
    printf("----Last modified at %s\n", ctime(&(fin_info.st_mtime)));

    // write back config file
    f_cfg = fopen(cfg_name, "w");
    fputs(cfg_comment, f_cfg);
    fputs(in_filename, f_cfg); fputc('\n', f_cfg);
    fputs(outdir_name, f_cfg);
    fclose(f_cfg);

//======================== header ========================
    char header[2] = {(char)0xc5, (char)0x84};

//======================== get data length ========================
    unsigned data_length, data_length_bit;
    char data_length_3B[3];
    data_length = fin_info.st_size;
    printf("Data length : %d B\n", data_length);
    data_length_bit = data_length *8;
    data_length_3B[0] = (uc)((data_length_bit >>16) &0x00ff);
    data_length_3B[1] = (uc)((data_length_bit >> 8) &0x00ff);
    data_length_3B[2] = (uc)((data_length_bit     ) &0x00ff);

//======================== get current time ========================
    time_t now = time(0);
    struct tm *our_tm = localtime(&now);
    char tm_6B[6];
    printf("Packing time: ");
    printf("%d-%d-%d ", (our_tm->tm_year - 100), (our_tm->tm_mon + 1), our_tm->tm_mday);
    printf("%d:%d:%d\n", our_tm->tm_hour, our_tm->tm_min, our_tm->tm_sec);
    tm_6B[0] = (uc)(our_tm->tm_year - 100);
    tm_6B[1] = (uc)(our_tm->tm_mon + 1);
    tm_6B[2] = (uc)(our_tm->tm_mday);
    tm_6B[3] = (uc)(our_tm->tm_hour);
    tm_6B[4] = (uc)(our_tm->tm_min );
    tm_6B[5] = (uc)(our_tm->tm_sec );
    
    char out_filename[160];
    char tmtemp[3];
    strcpy(out_filename, outdir_name);
    strcat(out_filename, "pkg--");
    itoa((our_tm->tm_mon + 1), tmtemp, 10); strcat(out_filename, tmtemp);
    strcat(out_filename, "_");
    itoa((our_tm->tm_mday   ), tmtemp, 10); strcat(out_filename, tmtemp);
    strcat(out_filename, "--");
    itoa((our_tm->tm_hour   ), tmtemp, 10); strcat(out_filename, tmtemp);
    strcat(out_filename, "_");
    itoa((our_tm->tm_min    ), tmtemp, 10); strcat(out_filename, tmtemp);
    strcat(out_filename, "_");
    itoa((our_tm->tm_sec    ), tmtemp, 10); strcat(out_filename, tmtemp);
    strcat(out_filename, ".bin");

    printf("Output file : %s\n", out_filename);
    FILE *fout = fopen(out_filename, "wb");
    fwrite(header, 1, 2, fout);
    fwrite(data_length_3B, 1, 3, fout);
    fwrite(tm_6B + 3, 1, 3, fout);
    
//======================== get crc ========================
    FILE *fin = fopen(in_filename, "rb");
    char data;
    unsigned short int_data, crc = 0;
    while(fread(&data, 1, 1, fin)){
        int_data = (int)(uc)data;
        crc = (crc << 8) ^crc16tab[((crc >> 8) ^int_data) &0x00ff];
        fwrite(&data, 1, 1, fout);
    }
    fclose(fin);
    char crcHB = (uc)((crc >>8) &0x00ff);
    char crcLB = (uc)((crc    ) &0x00ff);
    fwrite(&crcHB, 1, 1, fout);
    fwrite(&crcLB, 1, 1, fout);

//======================== supplement with 0 ========================
    char zero = 0;
    int zp;
    for(zp=0; zp<(data_length+10)%4; zp++)
        fwrite(&zero, 1, 1, fout);
    fclose(fout);

    printf("\n[P.S.] You can set output directory in setting file.\n");
    printf("\t----by Franco Lee. C\n");
    system("pause");
    return 0;
}
