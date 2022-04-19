n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        answer += 1
        cnt = 0

print(answer)