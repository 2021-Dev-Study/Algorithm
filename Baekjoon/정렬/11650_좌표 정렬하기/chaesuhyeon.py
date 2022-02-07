import sys
N = int(sys.stdin.readline())
num=[]
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    num.append([x, y])

num.sort() # [[1, -1], [1, 1], [2, 2], [3, 3], [3, 4]]

for i in range(N):
    print(num[i][0], num[i][1])


