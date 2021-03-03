from mx_lib import get_filename

print("Tran binary to hex_text_file.")

file_in = get_filename('Input file', 'iof/f_test2.bin')
file_out = str(file_in)[:-len(file_in.suffix)] + '.txt'
print(f'Output file: {file_out}')

# =========== main ==================
fout = open(file_out, 'w')
word = [0, 1, 2, 3]
reading = True
word_count = 0
mb_count = 0
with open(file_in, 'rb')as fin:
    while reading:
        for byte in range(4):
            data = fin.read(1)
            if data:
                word[byte] = data.hex().zfill(2)
            else:
                word[byte] = '00'
                reading = False
        if reading:
            out_word = '0x' + word[3] + word[2] + word[1] + word[0] + ',\n'
        else:
            out_word = '0x' + word[3] + word[2] + word[1] + word[0]
        fout.write(out_word)
        # monitor
        word_count += 1
        if word_count == 0x40000:
            mb_count += 1
            print(f'\r> {mb_count} MB')
            word_count = 0

fout.close()
print('==== End ====')
