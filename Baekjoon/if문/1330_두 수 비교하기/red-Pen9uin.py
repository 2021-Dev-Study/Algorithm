# 작성자: red-Pen9uin
# level 2: if statement
# 1330: 두 수 비교하기
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

def main():
    a, b = input().split()    # 입력받은 값을 공백을 기준으로 분리
    a = int(a)    # 변수를 정수로 변환한 뒤 다시 저장
    b = int(b)    # 변수를 정수로 변환한 뒤 다시 저장

    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("==")

if __name__ == "__main__":
	main()