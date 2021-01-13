
# get input file
while True:
    file_in = input('Input file: ')
    if not file_in:
        file_in = 'iof/f_test.bin'
    try:
        with open(file_in, 'rb') as ftest:
            break
    except FileNotFoundError:
        print('Can not find the file, try again, pls.')

for c in reversed(range(len(file_in))):
    if file_in[c] == '.':
        file_out = file_in[:c] + '_iq00' + file_in[c:]
        break
with open(file_out, 'wb') as f_flush:
    print(f'Output file: {file_out}')

fo = open(file_out, 'ab')

# trans bytes to binary
# new_byte_list = []
with open(file_in, 'rb') as fi:
    rd_n = 0
    MB_n = 0
    while True:
        rd_1B = fi.read(1)
        if not rd_1B:
            print(f'Read Done. {rd_n}B.')
            break
        rd_n = rd_n + 1
        if rd_n %1048576 == 0:      # 1MB
            MB_n = MB_n + 1
            print(f'{MB_n}MB,')
        int_1B = int(rd_1B.hex(), 16)
        # print('byte{:0>2d}: 0x{:0>2X}'.format(rd_n, int_1B))
        # separate 4bit|4bit
        byte_h4bit = (int_1B >> 4) &0x0f
        byte_l4bit = int_1B &0x0f
        # 0biqiq --> 0biq00_iq00
        bh_x1B = ((byte_h4bit << 4) ^(byte_h4bit << 2)) &0b11001100
        bl_x1B = ((byte_l4bit << 4) ^(byte_l4bit << 2)) &0b11001100
        # print('byte{:0>2d}: 0x{:0>2x}\n{:0>4b}_{:0>4b} --> {:0>8b}_{:0>8b}'\
        #     .format(rd_n, int_1B, byte_h4bit, byte_l4bit, bh_x1B, bl_x1B))
        fo.write(bytes([bh_x1B]))
        fo.write(bytes([bl_x1B]))
        # new_byte_list.append(bh_x1B)
        # new_byte_list.append(bl_x1B)

# write in file
# with open(file_out, 'wb') as fo:
#     for new_byte in new_byte_list:
#         fo.write(bytes([new_byte]))
#     len_nbl = len(new_byte_list)
#     print(f'Write Done. {len_nbl}B. Output file: {file_out}')
fo.close()

print('E N D\n')
