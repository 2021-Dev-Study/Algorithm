# 작성자: red-Pen9uin
# level 3: for statement
# 10871: X보다 작은 수
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

import sys

def main():
    num, x = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))

    for i in range(0,num):
        if a[i]<x:
            print(f"{a[i]}", end=' ')

if __name__ == "__main__":
    main()