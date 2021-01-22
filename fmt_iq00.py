from pathlib import Path
file_in_pre = 'iof/f_test.bin'
print("功能：二进制文件每两bit后添加2位0：iqiq --> iq00iq00")

# input file name
while True:
    file_in_s = input('Input file: ')
    if not file_in_s:
        file_in_s = file_in_pre
    else:
        file_in_s = ((repr(file_in_s))[1:-1]).replace('\\', '/')
    file_in = Path(file_in_s)
    if file_in.is_file():
        break
    else:
        print('Can not find the file, try again, pls.')

# output file name
for c in reversed(range(len(file_in_s))):
    if file_in_s[c] == '.':
        file_out_s = file_in_s[:c] + '_iq00' + file_in_s[c:]
        file_out = Path(file_out_s)
        break
with open(file_out, 'wb') as f_flush:
    print(f'Output file: {file_out}')
fo = open(file_out, 'ab')

# handle
byte_n = 0
MB_n = 0
with open(file_in, 'rb') as fi:
    while True:
        rd_1B = fi.read(1)
        if not rd_1B:
            break
        byte_n = byte_n + 1
        if byte_n %1048576 == 0:      # progress bar
            MB_n = MB_n + 1
            print(f'\r>{MB_n} MB')
        int_1B = int(rd_1B.hex(), 16)
        # print('byte{:0>2d}: 0x{:0>2X}'.format(byte_n, int_1B))
        # separate 4bit|4bit
        byte_h4bit = (int_1B >> 4) &0x0f
        byte_l4bit = int_1B &0x0f
        # 0bxxxx --> 0bxx00_xx00
        bh_x1B = ((byte_h4bit << 4) ^(byte_h4bit << 2)) &0b11001100
        bl_x1B = ((byte_l4bit << 4) ^(byte_l4bit << 2)) &0b11001100
        # print('byte{:0>2d}: 0x{:0>2x}\n{:0>4b}_{:0>4b} --> {:0>8b}_{:0>8b}'\
        #     .format(byte_n, int_1B, byte_h4bit, byte_l4bit, bh_x1B, bl_x1B))
        fo.write(bytes([bh_x1B]))
        fo.write(bytes([bl_x1B]))
    print(f'Done. Sum = {byte_n} B.')

fo.close()

end = input('\n==== END ====\nEnter anything to exit...')
