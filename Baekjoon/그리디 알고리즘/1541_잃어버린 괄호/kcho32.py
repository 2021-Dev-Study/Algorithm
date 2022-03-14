import sys

equation = sys.stdin.readline()
tmp_num = ""
add_flag = True
addition = 0
subtraction = 0

for ch in equation:
    if ch not in ['+', '-']:
        tmp_num += ch
    else:
        if ch == '-':
            if add_flag == True:
                add_flag = False
                addition += int(tmp_num)
                tmp_num = ""
            else:
                subtraction += int(tmp_num)
                tmp_num = ""
        else:
            if add_flag == True:
                addition += int(tmp_num)
                tmp_num = ""
            else:
                subtraction += int(tmp_num)
                tmp_num = ""

if add_flag == True:
    addition += int(tmp_num)
else:
    subtraction += int(tmp_num)

print(addition - subtraction)