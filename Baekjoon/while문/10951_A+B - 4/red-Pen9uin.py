# 작성자: red-Pen9uin
# level 4: while statement
# 10951: A+B - 4
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

def main():

    while True :
        try:
            a, b = map(int,sys.stdin.readline().split())
            print(a+b)
        except:
            # readline()은 입력값이 없을 시 EoF를 발생?
            # 해당 오류에 만났을 때 프로그램 종료
            break
    
if __name__ == "__main__":
    main()