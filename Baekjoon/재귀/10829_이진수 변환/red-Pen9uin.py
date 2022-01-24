# 작성자: red-Pen9uin
# level 10: Recursion
# 10829_이진수 변환
# 수행 결과:  KB / 	72 ms
"""
자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.

"""
# 재귀로 푼다는 건 계속 2로 나눈 수를 호출한다는 듯
# 이진수 9 == 1001

import sys


def binary_num(N: int) -> str:
    result = str(N%2)

    if N//2 > 0:
        ret = binary_num(N//2)
        result = ret + result
    
    return result


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(f"{binary_num(num)}")