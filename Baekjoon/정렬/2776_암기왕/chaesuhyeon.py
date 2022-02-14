import sys
input = sys.stdin.readline


t = int(input().rstrip())

for _ in range(t):
    n1 = int(input().rstrip())
    s1 = set(list(map(int,input().rstrip().split())))
    n2 = int(input().rstrip())
    s2 = list(map(int,input().rstrip().split()))
    for i in s2:
        if i in s1:
            print(1)
        else:
            print(0)