
file_in_pre = 'iof/f_test.bin'
print("功能：二进制文件每两bit后添加2位0：iqiq --> iq00iq00")

# input file name
while True:
    file_in = input('Input file: ')
    if not file_in:
        file_in = file_in_pre
    try:
        with open(file_in, 'rb') as ftest:
            break
    except FileNotFoundError:
        print('Can not find the file, try again, pls.')

# output file name
for c in reversed(range(len(file_in))):
    if file_in[c] == '.':
        file_out = file_in[:c] + '_iq00' + file_in[c:]
        break
with open(file_out, 'wb') as f_flush:
    print(f'Output file: {file_out}')
fo = open(file_out, 'ab')

# handle
rd_n = 0
MB_n = 0
with open(file_in, 'rb') as fi:
    while True:
        rd_1B = fi.read(1)
        if not rd_1B:
            break
        rd_n = rd_n + 1
        if rd_n %1048576 == 0:      # display per 1MB
            MB_n = MB_n + 1
            print(f'>{MB_n} MB')
        int_1B = int(rd_1B.hex(), 16)
        # print('byte{:0>2d}: 0x{:0>2X}'.format(rd_n, int_1B))
        # separate 4bit|4bit
        byte_h4bit = (int_1B >> 4) &0x0f
        byte_l4bit = int_1B &0x0f
        # 0bxxxx --> 0bxx00_xx00
        bh_x1B = ((byte_h4bit << 4) ^(byte_h4bit << 2)) &0b11001100
        bl_x1B = ((byte_l4bit << 4) ^(byte_l4bit << 2)) &0b11001100
        # print('byte{:0>2d}: 0x{:0>2x}\n{:0>4b}_{:0>4b} --> {:0>8b}_{:0>8b}'\
        #     .format(rd_n, int_1B, byte_h4bit, byte_l4bit, bh_x1B, bl_x1B))
        fo.write(bytes([bh_x1B]))
        fo.write(bytes([bl_x1B]))
    print(f'Done. Sum = {rd_n} B.')

fo.close()

end = input('\n==== END ====\nEnter anything to exit...')
