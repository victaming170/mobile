
file_in_pre = 'iof/f_test_less8.txt'
print("功能：补齐文本文档的每行的字符数。")

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
        n_pl = 8
    try:
        n_pl = int(n_pl)
        break
    except ValueError:
        print('Integer pls.')

# output file name
for c in reversed(range(len(file_in))):
    if file_in[c] == '.':
        file_out = file_in[:c] + '_' + str(n_pl) + 'x' + c_pl + file_in[c:]
        break
with open(file_out, 'w') as f_flush:
    print(f'Output file: {file_out}')
fo = open(file_out, 'a')

# handle
line_n = 0
# spy_step = 1000
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
