# 작성자: red-Pen9uin
# level 10: Recursion
# 19947_투자의 귀재 배주형
# 수행 결과: 30864 KB / 68 ms
"""
문제 링크:
https://www.acmicpc.net/problem/19947

첫째 줄에 초기 비용 H와 투자 기간 Y가 주어진다.
모든 입력은 정수로 주어진다.

가장 많은 이득을 얻었을 때의 총 자산을 소수점을 모두 버리고 정수로 출력한다.
"""

import sys


def solve(money, years_left, ABC):
    interest = [(1, 1.05), (3, 1.20), (5, 1.35)]
    max_num = 0

    if years_left < 0:
        return int(money)
    elif years_left == 0:
        return int(money*ABC)
    
    for abc in interest:
        temp = solve(money, years_left-abc[0], abc[1])
        if max_num < temp:
            max_num = temp

    return int(max_num*ABC)

if __name__ == "__main__":
    initial_money, years_left = map(int, sys.stdin.readline().split())

    ret = solve(initial_money, years_left, 1.0)
    print(f"{int(ret)}")