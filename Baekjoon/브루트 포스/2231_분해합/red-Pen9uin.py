# 작성자: red-Pen9uin
# level 11: brute force
# 2231_분해합
# 수행 결과: 30864 KB / 68 ms
"""
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
"""

import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    digit = len(str(num))
    
    start_num = num - digit*9

    for now in range(start_num, num):
        if now < 0:
            continue
        decompose = list(str(now))
        decompose = list(map(int, decompose))
        result = sum(decompose) + now
        if result == num:
            print(now)
            exit()
    print(0)
