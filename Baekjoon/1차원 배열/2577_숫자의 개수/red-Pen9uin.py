# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 2577: 숫자의 개수
"""
세 개의 자연수 A, B, C가 주어질 때
A x B x C를 계산한 결과에
0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

"""
import sys

def main():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())

    result = A*B*C
    result = str(result)

    count = [0]*10
    
    for i in range(0, len(result)):
        count[int(result[i])] += 1
    
    for i in range(0,10):
        print(count[i])

if __name__ == "__main__":
    main()