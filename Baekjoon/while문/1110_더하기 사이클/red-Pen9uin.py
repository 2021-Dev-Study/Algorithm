# 작성자: red-Pen9uin
# level 4: while statement
# 1110: 더하기 사이클
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

import sys

def main():
    num = int(sys.stdin.readline())
    temp = num
    new = sum = cycle = 0
    
    while True :
        sum = temp//10 + temp%10
        new = (temp%10)*10 + sum%10
        temp = new
        cycle += 1
        # print(f"{sum}, {new}, {cycle}")
        if new == num:
            break
    print(cycle)
    
if __name__ == "__main__":
    main()