import sys
N = int(sys.stdin.readline())
schedule = []
for _ in range(N) :
    schedule.append(list(map(int, sys.stdin.readline().split())))
#당연히 시작 순으로 먼저 정렬하고
# # 회의 간격이 짧은 순으로 다시 정렬해서
# ex. ___ _____ ___ __ _____
#   __ ___ ___ _____ ___ ____
# 가장 앞쪽 회의부터 끝나자마자  최대한 빨리 시작할 수 있는 회의들을 이어붙이기
schedule.sort(key= lambda x : x[0])
schedule.sort(key = lambda x : x[1])
last = 0
cnt = 0
for st, lt in schedule:
    if st >= last:
        cnt += 1
        last = lt
print(cnt)
# mx = 0
# for s in schedule :
#     start = s[0]
#     while True :
