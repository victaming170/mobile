
filein = '1.txt'
lines = []
print("功能：用0补齐文本文件每行字符数")
while True:
    filein = input("input the filename: ")
    try:
        with open(filein, 'r') as fpr:
            lines = fpr.readlines()
        break
    except FileNotFoundError:
        print('Can not find the file, try again.')

while True:
    n_pl = input("input the num_per_line: ")
    try:
        n_pl = int(n_pl)
        break
    except ValueError:
        print('Integer pls.')

for i in range(len(lines)):
    if lines[i][-1] == '\n':
        n_pl_real = n_pl + 1
    else:
        n_pl_real = n_pl
        print(i+1, '=last line')
    if len(lines[i]) < n_pl_real:
        lines[i] = (n_pl_real - len(lines[i])) * '0' + lines[i]

fileout = 'fmt_' + str(n_pl) + '_' + filein
with open(fileout, 'w') as fout:
    for line in lines:
        fout.write(line)

print('Success. Output: ', fileout)

