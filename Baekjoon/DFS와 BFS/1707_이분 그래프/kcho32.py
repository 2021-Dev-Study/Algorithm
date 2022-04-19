import sys


tc = int(input())

for i in range(tc):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    tmp = [[] for _ in range(v + 1)]
    
    for i in range(e):
        first, second = map(int, sys.stdin.readline().rstrip().split())
        tmp[first].append(second)
        tmp[second].append(first)
    
    print(tmp)
