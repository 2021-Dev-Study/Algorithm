# 작성자: red-Pen9uin
# level 10: Recursion
# 18511_큰 수 구성하기
# 수행 결과: 32420 KB / 120 ms
"""
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오.
K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고,
K={1, 5, 7}일 때
답은 577이다.


첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다.
(10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3)
둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다.
각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.

첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.

"""
import sys
from collections import deque

def get_big_number(num: deque, count: int, stack:deque) -> list:
    makeable = list()
    my_num = deque(num)

    if len(stack)!=0:
        temp = "".join(map(str, stack))
        makeable.append(temp)
        if len(stack)==count:
            return makeable
    
    
    for i in range(len(my_num)):
        stack.append(my_num[0])
        makeable += get_big_number(num, count, stack)
        stack.pop()
        my_num.rotate(1)

    return makeable

if __name__ == "__main__":
    limit, count = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))

    # limit의 자릿수를 구하는 코드
    cnt = 1
    tmp = limit
    while True:
        if tmp//10>0:
            cnt+=1
            tmp //= 10
        else:
            break
    
    stack = deque()
    result = get_big_number(num, cnt, stack)

    result = set(result)
    result = list(map(int, result))
    max_num = result[0]

    # print(sorted(result))

    for i in result:
        if i <= limit:
            if i >= max_num:
                max_num = i

        if max_num > limit:
            max_num = i
    print(max_num)