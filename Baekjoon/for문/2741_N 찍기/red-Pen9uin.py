# 작성자: red-Pen9uin
# level 3: for statement
# 2741: N 찍기
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

import sys

def main():
    num = int(sys.stdin.readline())

    for i in range(1, num+1):
        print(f"{i}")

if __name__ == "__main__":
	main()