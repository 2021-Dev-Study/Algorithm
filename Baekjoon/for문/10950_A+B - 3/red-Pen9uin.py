# 작성자: red-Pen9uin
# level 3: for statement
# 10950: A+B - 3
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

def main():
    num = int(input())
    num_list = list()
    for i in range(0, num):
        num_list.append(input().split())

    for i in range(0,num):
        num_list[i] = list(map(int, num_list[i]))
        print(f"{num_list[i][0] + num_list[i][1]}")


if __name__ == "__main__":
	main()