# 1931
n = int(input())
shedule = [list(map(int, input().split())) for _ in range(n)]
shedule.sort(key = lambda x: x[0])
shedule.sort(key = lambda x: x[1])

cnt = 1
end = shedule[0][1]
for i in range(1, n):
  if shedule[i][0] >= end:
    cnt += 1
    end = shedule[i][1]

print(cnt)