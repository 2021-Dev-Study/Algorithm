# 작성자: red-Pen9uin
# level 2: if statement
# 14681: 사분면 고르기
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

def main():
    # x, y = input().split()    # 입력받은 값을 공백을 기준으로 분리
    # x = int(x)    # 변수를 정수로 변환한 뒤 다시 저장
    # y = int(y)    # 변수를 정수로 변환한 뒤 다시 저장
    # x = int(input())
    # y = int(input())
    x = input()
    y = input()

    x = int(x)
    y = int(y)

    if(x>0 and y>0):
        print('1')
    elif(x<0 and y>0):
        print('2')
    elif(x<0 and y<0):
        print('3')
    elif(x>0 and y<0):
        print('4')

    # else:
    #     print("What is happening...?")

if __name__ == "__main__":
	main()