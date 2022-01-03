# 작성자: red-Pen9uin
# level 10: Recursion
# 10870: 피보나치 수 5
"""
피보나치 수는 0과 1로 시작한다.
0번째 피보나치 수는 0이고,
1번째 피보나치 수는 1이다.
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

"""
# 피보나치 문제에서 주로 크게 고민되는 부분은 자료형이었던 것으로 기억한다.
# 파이썬은 자료형을 자동으로 잡아주기에, 자료형에 대한 고민을 하지 않을 수 있다.
# 

import sys

def get_fibonacci(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        before_num = 0
        now_num = 1
        i = 2
        while i < num+1 :
            new_num = before_num+now_num
            before_num = now_num
            now_num = new_num
            i += 1
        return new_num

def get_fibonacci_recursion(cnt: int, now: int=0) -> int:
    # 재귀함수를 이용한 버전
    # 메모리를 미친듯이 먹을 것 같다.
    if cnt == 0:
        return 0
    elif cnt == 1:
        return 1
    else:
        return get_fibonacci_recursion(cnt-2) + get_fibonacci_recursion(cnt-1)

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(get_fibonacci_recursion(num))
