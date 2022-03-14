# 단계별 - 그리디 알고리즘
# 1931_회의실 배정
import sys
if __name__ == "__main__":
    N = int(input())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    
    # 회의들을 빨리 끝나는 회의 순서대로, 빨리 시작하는 순서대로 정렬하기
    times.sort(key = lambda x:(x[1],x[0]))

    cnt = 1
    end = times[0][1]
    for i in range(1, N):
        if times[i][0] >= end: # 이전 회의의 끝나는 시간보다 지금 회의의 시작하는 시간이 더 늦다면
            cnt += 1 # 회의 수 증가하고
            end = times[i][1] # 회의 종료 시간 갱신
    print(cnt)