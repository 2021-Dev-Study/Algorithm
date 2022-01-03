# 작성자: red-Pen9uin
# level 10: Recursion
# 10872: 팩토리얼
"""
0보다 크거나 같은 정수 N이 주어진다.
이때, N!을 출력하는 프로그램을 작성하시오.

"""
# 너무 간단하고 유명한 예제라 외운 대로 풀이하였으나,
# 재귀함수를 이용하는 방식은 채점이 어려운 면이 있는 것 같아 반복문으로 다시 구현함.

import sys

def get_factorial(num: int) -> int:
    if num<=1 :
        return 1
    else:
        return num * get_factorial(num-1)

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(get_factorial(num))
    # i = num
    # result = 1
    # while i > 0:
    #     result = result*i
    #     i -= 1

    # print(result)