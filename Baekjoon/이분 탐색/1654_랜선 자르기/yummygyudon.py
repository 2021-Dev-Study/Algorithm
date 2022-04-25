import sys

input = sys.stdin.readline
N, M = map(int, input().split())
LAN = []
for _ in range(N):
    LAN.append(int(input()))
start = 1
end = max(LAN)

while start <= end:
    ea = 0
    mid = (start + end) // 2

    for l in LAN:
        if l >= mid:
            ea += (l // mid)
    if ea < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)