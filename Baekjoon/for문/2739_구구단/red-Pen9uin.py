# 작성자: red-Pen9uin
# level 3: for statement
# 2739: 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

def main():
    num = int(input())

    for i in range(1,10):
        print(f"{num} * {i} = {num*i}")

if __name__ == "__main__":
	main()