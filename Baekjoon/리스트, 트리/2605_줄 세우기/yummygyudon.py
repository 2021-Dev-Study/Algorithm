import sys
input = sys.stdin.readline
N = int(input())
ls = list(map(int, input().split()))
pick = list(enumerate(ls, 1))
line = []
cnt = 0
while cnt < N :
    line_num, pick_num = pick[cnt]
    if pick_num == 0 :
        line.append(line_num)
        cnt+=1
    else :
        line.append(line_num)
        for i in range(len(line)-1, len(line)-pick_num-1, -1) :
            line[i] = line[i-1]
        line[len(line)-pick_num-1] = line_num
        cnt += 1
for n in line :
    print(n, end=' ')

'''
[(1, 0), (2, 1), (3, 1), (4, 3), (5, 2)]
line_num : 1  pick_num : 0
[1]

line_num : 2  pick_num : 1
[1, 2]
[2, 1]

line_num : 3  pick_num : 1
[2, 1, 3]
[2, 3, 1]

line_num : 4  pick_num : 3
[2, 3, 1, 4]
[4, 2, 3, 1]

line_num : 5  pick_num : 2
[4, 2, 3, 1, 5]
[4, 2, 5, 3, 1]

4 2 5 3 1 
'''