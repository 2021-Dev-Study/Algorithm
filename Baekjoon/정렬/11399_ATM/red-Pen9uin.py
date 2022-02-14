# 작성자: red-Pen9uin
# Classification: sort algorithm
# 11399_ATM
# 수행 결과: 30864 KB / 68 ms
"""
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

"""

import sys

def solution(waiting):
    length = len(waiting)

    waiting = sorted(waiting)
    wait_time = 0

    for i in range(0, length):
        wait_time += (length - i) * waiting[i]
    
    return wait_time


if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    waiting = list(map(int, sys.stdin.readline().split()))
    # waiting = [None] * cnt
    # for i in range(cnt):
    #     waiting[i] = int(sys.stdin.readline().split())

    wait_time = solution(waiting)
    print(f"{wait_time}")