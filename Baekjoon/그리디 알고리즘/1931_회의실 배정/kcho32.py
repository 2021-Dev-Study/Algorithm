# import time
# start = time.time()
# # meetings: 회의 갯수
# # schedules: 입력 받은 회의 스케줄을 끝나는 시간으로 정렬
# meetings = int(input())
# schedules = sorted([tuple(map(int, input().split())) for _ in range(meetings)], key=lambda x: (x[1], x[0]))
# start_time = 0 # 시작점을 0으로 초기화 후 시작
# count = 0 # 회의 수

# #회의를 많이 하려면 일단 제일 먼저 끝나는 것을 겹치지 않게 고르는 것이 좋을 것 같아서 끝나는 순으로 정렬
# for schedule in schedules:
#     # 그리디 알고리즘을 통해 일단 가장 빨리 끝낼 수 있는 것들만 고르는 것으로 일단 실행해봄
#     if schedule[0] >= start_time:
#         count += 1
#         start_time = schedule[1]

# print(count)
# print("time: ", time.time() - start)

# schedules를 정렬할 때 끝나는 시간 뿐이 아닌 시작 시간 또한 정렬해줘야 한다
# 예를 들어 7 7과 4 5, 5 7이 나올 경우 7 7이 먼저 선택될 수 있기 때문 
# 처음에 끝나자마자 같은 시간에 시작이 안되는 줄 알고 안해서 생긴 오류

# 위에 것이 너무 시간을 잡아 먹어서 다른 버전 한번 사용



import time
start = time.time()

import sys

meetings = int(sys.stdin.readline())
schedules = []
# 이게 훨씬 빠름...
for _ in range(meetings):
    x, y = map(int, sys.stdin.readline().split())
    schedules.append((x, y))

schedules.sort(key=lambda x: (x[1], x[0]))
start_time = 0 # 시작점을 0으로 초기화 후 시작
count = 0 # 회의 수

for schedule in schedules:
    # 그리디 알고리즘을 통해 일단 가장 빨리 끝낼 수 있는 것들만 고르는 것으로 일단 실행해봄
    if schedule[0] >= start_time:
        count += 1
        start_time = schedule[1]

print(count)

print("time: ", time.time() - start)


## 결국 위에 것도 인풋을 sys.stdin.readline()으로 받으니 시간은 둘 다 또이또이 했다 -> 시간 낭비