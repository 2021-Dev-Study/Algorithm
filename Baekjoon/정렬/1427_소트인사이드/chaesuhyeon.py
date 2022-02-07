import sys
N = list(map(int, sys.stdin.readline())) # 2413 --> [2, 4, 1, 3]
N.sort(reverse=True)
for i in range(len(N)):
    print(N[i], end='')
