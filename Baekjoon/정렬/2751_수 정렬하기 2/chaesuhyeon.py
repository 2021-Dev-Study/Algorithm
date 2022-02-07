# pypy3 
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()
for i in range(len(num)):
    print(num[i])