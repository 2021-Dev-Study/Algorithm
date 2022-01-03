# 작성자: red-Pen9uin
# level 7: String
# 2908: 상수
"""
상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
예를 들어, 734와 893을 칠판에 적었다면,
상수는 이 수를 437과 398로 읽는다.

따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

상근이는 수의 크기를 비교하는 문제를 내주었다.
두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

"""
import sys

if __name__ == "__main__":
    A, B = sys.stdin.readline().split()
    # split()을 통해 만들어진 문자열은 끝에 추가적인 문자를 가지고 있지 않는 것 같다
    
    # python은 slicing을 통해 정말 쉽게 할 수 있다...
    A_new = int(A[::-1])
    B_new = int(B[::-1])
    
    print(A_new if A_new>B_new else B_new)