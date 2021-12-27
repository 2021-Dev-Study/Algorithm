# 작성자: red-Pen9uin
# level 3: for statement
# 15552: 빠른 A+B

# C++을 사용하고 있고 cin/cout을 사용하고자 한다면,
# cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고,
# endl 대신 개행문자(\n)를 쓰자.
# 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등
# C의 입출력 방식을 사용하면 안 된다.

# Java를 사용하고 있다면,
# Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다.
# BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

# Python을 사용하고 있다면,
# input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에
# 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

import sys

def main():
    num = int(sys.stdin.readline())
    num_list = list()
    for i in range(0, num):
        num_list.append(list(map(int, sys.stdin.readline().split())))

    for i in range(0,num):
        print(f"{num_list[i][0] + num_list[i][1]}")


if __name__ == "__main__":
	main()