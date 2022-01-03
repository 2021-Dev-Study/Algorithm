# 작성자: red-Pen9uin
# level 3: for statement
# 11021: A+B - 7
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

def main():
    num = int(sys.stdin.readline())
    num_list = list()
    for i in range(0, num):
        num_list.append(list(map(int, sys.stdin.readline().split())))

    for i in range(0,num):
        num_list[i] = list(map(int, num_list[i]))
        print(f"Case #{i+1}: {num_list[i][0] + num_list[i][1]}")


if __name__ == "__main__":
	main()