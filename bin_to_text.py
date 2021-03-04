from pathlib import Path

# ============= import function from mx_lib===================
# display_=[str], dir_mode_=[bool], default_=[str(path)]
def get_filename(display_, default_='', dir_mode_=False):
    while True:
        print(display_)
        str_in = input('>>> ')
        if not str_in:
            str_in = default_
        file_Path = Path(str_in)
        if dir_mode_ and file_Path.is_dir():
            return file_Path
        elif file_Path.is_file():
            return file_Path
        else:
            print(f'Can not find {file_Path}, try again pls.')

# =============================================================
# ==================== code body ==============================
# =============================================================
welcome = '= Tran binary_file to text_file. ='
print(len(welcome) *'=')
print(welcome)
print(len(welcome) *'=')

# config
file_out_total = 5      # how many output file
out_suffix = '.coe'     # suffix of output file
size_of_line = 4        # how many bytes in every line, unit = Byte.

file_out_beginning = 'memory_initialization_radix = 16;\nmemory_initialization_vector = \n'
file_out_end = ';'

line_beginning = ''
line_end = ',\n'

monitor_line_node = 256    # progress bar, show current progress every [%] lines
line_limit = 1024           # when line_counter come to line_limit, close current output file

# get input file
file_in = get_filename('Input file', 'iof/f_test.bin')      # type(file_in) = Class Path
fin = open(file_in, 'rb')

# main loop
for file_out_i in range(file_out_total):
    # get new output file
    file_out = str(file_in)[:-len(file_in.suffix)] + '-' + str(file_out_i) + out_suffix
    print(f'Output file {file_out_i}: {file_out}')
    fout = open(file_out, 'w')
    # write at the very beginning
    fout.write(file_out_beginning)

    line_byte_list = size_of_line *[0]
    working = True
    line_cnt = 0
    node_cnt = 0
    while working:
        for byte_n in range(size_of_line):
            one_byte = fin.read(1)
            if one_byte:
                line_byte_list[byte_n] = one_byte.hex().zfill(2)
            else:
                # end of read
                line_byte_list[byte_n] = '00'
                working = False
                print('End of reading.')
        output_line = line_beginning
        for i in reversed(range(size_of_line)):
            output_line += line_byte_list[i]
        # monitor
        line_cnt += 1
        if line_cnt %monitor_line_node == 0:
            node_cnt += 1
            print(f'> {node_cnt} *{monitor_line_node} lines')
        # check end of write
        if line_cnt == line_limit:
            working = False
            print('End of writing.')
        # write in file
        if working:
            output_line += line_end
        else:
            output_line += file_out_end
        fout.write(output_line)
    # one output file ready
    fout.close()
    print()

fin.close()
print('======== End ========')
