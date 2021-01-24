from pathlib import Path
file_in_pre = 'iof/f_test.txt'
print("功能：补齐文本文档的每行的字符数。")

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

# get char
while True:
    c_pl = input("The char needed to add(default'0'): ")
    if not c_pl:
        c_pl = 0
    c_pl = str(c_pl)
    if len(c_pl) == 1:
        break
    print('Single char pls.')

# get how many chars per line
while True:
    n_pl = input("The num_per_line(default8): ")
    if not n_pl:
        n_pl = '8'
    if n_pl.isdigit():
        n_pl = int(n_pl)
        break
    else:
        print('Integer pls.')

# output file name
for c in reversed(range(len(file_in_s))):
    if file_in_s[c] == '.':
        file_out_s = file_in_s[:c] + '_' + str(n_pl) + 'x' + c_pl + file_in_s[c:]
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
        if line[-1] == '\n':
            n_pl_real = n_pl + 1
        else:
            n_pl_real = n_pl
        if len(line) < n_pl_real:
            line = (n_pl_real - len(line)) * c_pl + line
        fo.write(line)
    print(f'Done. Sum = {line_n} rows.')

fo.close()

end = input('\n==== END ====\nEnter anything to exit...')
