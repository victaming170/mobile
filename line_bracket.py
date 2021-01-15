
file_in_pre = 'iof/f_test_nobracket.txt'
print("功能：在文本文件的每一行首尾加字符。")

# input file name
while True:
    file_in = input('Input file: ')
    if not file_in:
        file_in = file_in_pre
    try:
        with open(file_in, 'r') as ftest:
            break
    except FileNotFoundError:
        print(f'Can not find the "{file_in}", try again, pls.')

bs = input('String added at the beginning of each line: ')
es = input('String added at the end of each line(except the last line): ')

# output file name
for c in reversed(range(len(file_in))):
    if file_in[c] == '.':
        file_out = file_in[:c] + '_brkt' + file_in[c:]
        break
with open(file_out, 'w') as f_flush:
    print(f'Output file: {file_out}')
fo = open(file_out, 'a')

# handle
line_n = 0
line_k = 0
with open(file_in, 'r') as fi:
    while True:
        line = fi.readline()
        if (not line) or (line == '\n'):
            break
        line_n = line_n + 1
        if line_n %1000 == 0:
            line_k = line_k + 1
            print(f'>{line_k}kilo rows.')       # display per 1000 rows
        if line[-1] != '\n':
            line = bs + line
        else:
            line = bs + line[:-1] + es + '\n'
        fo.write(line)
    print(f'Done. Sum = {line_n} rows.')
fo.close()

end = input('\n==== END ====\nEnter anything to exit...')