# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 1931_회의실 배정

"""
https://www.acmicpc.net/problem/1931
"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys
from collections import deque

def solution(num, time):
    # 회의 목록 모두 정렬 (1. 끝나는시간 2. 시작시간)
    # O(N*logN) + O(N*logN)
    time.sort()
    time.sort(key= lambda x: x[1])
    time_table = deque(time)

    # 가장 빨리 끝나는 회의 하나를 우선적으로 예약
    reserve = []
    reserve.append(time_table.popleft())

    # O(N)
    for _ in range(num-1):
        # 검토할 다음 회의
        temp = time_table.popleft()
        
        # 배정된 회의가 끝나지 않았음
        if temp[0] < reserve[-1][1]:
            print(f"{temp} nothing happened...")
            continue
        
        # 이후: 배정된 회의가 끝났음
        # temp[0] >= reserve[-1][1]
        # 예약에 집어넣음
        reserve.append(temp)

        # 예약잡아둔 회의보다 더 빨리 끝나는 경우, 우선예약..
        # 을 의도했으나 로직이 바뀌며 쓸모없어진 코드.
        # if reserve[-1][1] > temp[1]:
        #     reserve.pop()
        #     reserve.append(temp)
        
    return len(reserve)


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    time = [None] * num
    for i in range(num):
        time[i] = list(map(int, sys.stdin.readline().split()))

    print(solution(num, time))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""