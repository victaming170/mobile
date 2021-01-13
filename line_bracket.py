
filename = '0.txt'
lines = []
print("功能：在文本文件的每一行首尾加字符")
while True:
    filename = input("input the filename: ")
    try:
        with open(filename, 'r') as fpr:
            lines = fpr.readlines()
        break
    except FileNotFoundError:
        print('Can not find the file, try again.')

bs = input('String added at the beginning of each line: ')
es = input('String added at the end of each line(except the last line): ')

for i in range(len(lines)):
    if i != (len(lines)-1):     # if it isn't the last line
        lines[i] = bs + lines[i][:-1] + es +lines[i][-1]
    else:
        lines[i] = bs + lines[i]

outfile = 'brkt_' + filename
with open(outfile, 'w') as fpw:
    for line in lines:
        fpw.write(line)

print(f'Success. Output file: {outfile}\n')

print('==== E N D ====\n')

