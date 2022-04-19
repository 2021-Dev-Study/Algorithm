import sys
N, Money = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N) :
    coin.append(int(sys.stdin.readline()))

coin.sort(reverse = True)
cnt = 0
idx = 0
while Money > 0 :
    m = Money // coin[idx]
    if m > 0 :
        cnt += m
        Money = Money - m*coin[idx]
    idx += 1
print(cnt)