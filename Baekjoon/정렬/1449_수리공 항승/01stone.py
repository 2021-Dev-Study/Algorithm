# 1449 : 수리공 항승

n, l = map(int, input().split())
location = list(map(int, input().split()))
location.sort()

start = 0
cnt = 0

for x in location:
  if start < x:        # 0 < 1
                       # 현재 위치가 기존에 붙인 테이프의 길이보다 앞에 있으면 
    start = x + l - 1  # start = 1 + 2 - 1
                       # 테이프 시작점을 지금으로 바꾸고
    cnt += 1           # 테이프를 붙임

print(cnt)