from pathlib import Path
file_in_pre = 'iof/f_test.txt'
print("功能：在文本文件的每一行首尾加字符。")

# input file name
while True:
    file_in_s = input('Input file: ')
    if not file_in_s:
        file_in_s = file_in_pre
    file_in = Path(file_in_s)
    if file_in.is_file():
        break
    else:
        print(f'Can not find the "{file_in}", try again, pls.')

bs = input('String added at the beginning of each line: ')
es = input('String added at the end of each line(except the last line): ')

# output file name
for c in reversed(range(len(file_in_s))):
    if file_in_s[c] == '.':
        file_out_s = file_in_s[:c] + '_brkt' + file_in_s[c:]
        break
file_out = Path(file_out_s)
fo = open(file_out, 'w')
print(f'Output file: {file_out}')

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
            print(f'>{line_k}kilo rows.')       # progress bar
        if line[-1] != '\n':
            line = bs + line
        else:
            line = bs + line[:-1] + es + '\n'
        fo.write(line)
    print(f'Done. Sum = {line_n} rows.')
fo.close()

end = input('\n==== END ====\nEnter anything to exit...')
