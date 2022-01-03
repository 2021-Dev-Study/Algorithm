# 작성자: red-Pen9uin
# level 3: for statement
# 2439: 별 찍기 - 2
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

import sys

def main():
    num = int(sys.stdin.readline())

    for i in range(1, num+1):
        print(" "*(num-i) + "*"*i)

if __name__ == "__main__":
    main()