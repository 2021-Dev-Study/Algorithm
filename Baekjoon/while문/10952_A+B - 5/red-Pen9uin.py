# 작성자: red-Pen9uin
# level 4: while statement
# 10952: A+B - 5
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

def main():

    while True :
        a, b = map(int,sys.stdin.readline().split())
        if a==0 and b==0 :
            break
        else:
            print(a+b)
    
if __name__ == "__main__":
    main()