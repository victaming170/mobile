// my c lib
#include <sys/stat.h>
#include <time.h>


void get_inpath(char *inpath_buff_, const char *default_inpath_){
    struct _stat fin_info;
    char scan_str[128];
    while(1){
        printf("Input file >>> ");
        gets(scan_str);
        if(strlen(scan_str) == 0)
            strcpy(scan_str, default_inpath_);
        if((_stat(scan_str, &fin_info) == 0) &&(fin_info.st_mode &S_IFREG))
            break;
        else
            printf("!!! The file doesn't exist. Try again, pls.\n");
    }
    printf("Get input file : %s\n", scan_str);
    printf("~~~Last modified at %s", ctime(&(fin_info.st_mtime)));
    strcpy(inpath_buff_, scan_str);
}


void get_outpath(char *outpath_buff_){
    struct _stat out_info;
    char out_dir[128], out_name[64], full_path[192];
    char scan[128];
    printf("You can indicate the output directory and filename. Or load default by press Enter only.\n");
    // get directory
    printf("Default output dir: ./ >>> ");
    gets(scan);
    int scan_len = strlen(scan);
    if(scan_len == 0)
        strcpy(out_dir, "./");
    else{
        if((_stat(scan, &out_info) == 0) &&(out_info.st_mode &S_IFDIR)){
            if((scan[scan_len-1] != '/') &&(scan[scan_len-1] != '\\')){     // if string is not end in '/' or '\'
                scan[scan_len+1] = '\0';
                scan[scan_len  ] = '/';
            }
            strcpy(out_dir, scan);
        }
        else if((_stat(scan, &out_info) == 0) &&(out_info.st_mode &S_IFREG)){
            strcpy(outpath_buff_, scan);
            return;
        }
    }
    strcpy(out_dir, scan);
    // get filename
    printf("Default filename: out_getput >>> ");
    gets(scan);
    scan_len = strlen(scan);
    if(scan_len == 0)
        strcpy(out_name, "out_getput");
    else
        strcpy(out_name, scan);
    // joint dir and filename
    strcpy(full_path, out_dir);
    strcat(full_path, out_name);
    strcpy(outpath_buff_, full_path);
    return;
}

