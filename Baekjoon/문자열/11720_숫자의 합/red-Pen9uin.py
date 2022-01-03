# 작성자: red-Pen9uin
# level 7: String
# 11720: 숫자의 합
"""
N개의 숫자가 공백 없이 쓰여있다.
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

"""
import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    num_string = sys.stdin.readline()
    result = 0
    for i in range(0, num):
        result += int(num_string[i])
    print(result)