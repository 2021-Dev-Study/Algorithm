# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 3052: 나머지
"""
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

"""
import sys

def main():
    # arr = list()
    remain = list()
    DIVIDE = 42
    for i in range(0,10):
        num = int(sys.stdin.readline())
        remain.append(num % DIVIDE)

    remain = set(remain)

    print(len(remain))

if __name__ == "__main__":
    main()