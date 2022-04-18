# 이게 왜 이진 탐색..??
# 공유기 간의 거리를 이진 탐색으로 구하는 것!!!

import sys
if __name__ == "__main__":
    N, C = map(int, input().split())
    home = [0] * N
    for i in range(N):
        home[i] = int(sys.stdin.readline().replace('\n', ''))

    home.sort() # 이진 탐색을 위한 정렬

    start = 1
    end = home[-1] - home[0]  # end값은 공유기간의 최대 거리
    result = 0
    while start <=  end:
        mid = (start+end)//2  # 공유기간의 gap

        tmp = home[0] # 일단 가장 앞에 있는 집에는 공유기를 무조건 설치하기
        cnt = 1 # 설치된 공유기 수

        for i in range(1, N): # 가장 앞에 있는 집 제외 나머지 집에 대하여
            # 현재 집과 공유기가 마지막으로 설치된 집 사이의 거리가 공유기간의 gap보다 크거나 같다면 현재 집에 공유기 설치
            if home[i] - tmp >= mid: 
                cnt += 1
                tmp = home[i]
        
        if cnt < C: #설치된 공유기 수가 목표치보다 작다면 공유기간의 gap 줄이기
            end = mid-1
        else: # 설치된 공유기 수가 목표치보다 크다면 공유기간의 gap 늘리기
            start = mid + 1
            result = mid # 일단 답이 될 수 있는 경우니 result에 저장


    print(result)

