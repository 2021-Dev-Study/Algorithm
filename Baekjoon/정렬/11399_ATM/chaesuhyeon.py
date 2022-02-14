import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split())) # 시간 입력받음
arr.sort() # 정렬

time = [0] * N
t_sum = 0
for i in range(N):
    t_sum += arr[i] # 시간의 합계를 구해줘서
    time[i] = t_sum # time리스트에 각 사람이 걸리는 시간의 합을 넣어줌
print(sum(time)) # 리스트 전체 합 구해줌 (모든 사람의 시간의 합)
