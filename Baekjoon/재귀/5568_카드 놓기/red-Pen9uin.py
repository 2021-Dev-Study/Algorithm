# 작성자: red-Pen9uin
# level 10: Recursion
# 5568_카드 놓기
# 수행 결과: 32396 KB / 96 ms
"""
상근이는 카드 n(4 ≤ n ≤ 10)장을 바닥에 나란히 놓고 놀고있다.
각 카드에는 1이상 99이하의 정수가 적혀져 있다.
상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고,
가로로 나란히 정수를 만들기로 했다.

상근이가 만들 수 있는 정수는 모두 몇 가지일까?

예를 들어, 카드가 5장 있고,
카드에 쓰여 있는 수가 1, 2, 3, 13, 21라고 하자.
여기서 3장을 선택해서 정수를 만들려고 한다.
2, 1, 13을 순서대로 나열하면 정수 2113을 만들 수 있다.
또, 21, 1, 3을 순서대로 나열하면 2113을 만들 수 있다.
이렇게 한 정수를 만드는 조합이 여러 가지 일 수 있다.

n장의 카드에 적힌 숫자가 주어졌을 때,
그 중에서 k개를 선택해서 만들 수 있는 정수의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 n이, 둘째 줄에 k가 주어진다. 셋째 줄부터 n개 줄에는 카드에 적혀있는 수가 주어진다.
첫째 줄에 상근이가 만들 수 있는 정수의 개수를 출력한다.

"""
# 재귀와 스택?
"""
a b / c d 
a b c / d / 남은개수만큼만 반복
a b d / c
a c d
b c d

n n+1 n+2
n n+1 n+3
n n+2 n+3
...
n+1 n+2 n+3

"""

import sys
from collections import deque
# stack = list()

def make_numbers(card, select_till, selected):
    stack = list()

    if len(selected)==select_till:
        temp = "".join(map(str, selected))
        stack.append(temp)
        return stack

    for i in range(0, len(card)):
        selected.append(card.popleft())
        stack += make_numbers(card, select_till, selected)
        card.append(selected.pop())
    
    return stack


if __name__ == "__main__":
    card_total = int(sys.stdin.readline())
    select_till = int(sys.stdin.readline())
    card = deque()
    selected = deque()

    for i in range(card_total):
        card.append(int(sys.stdin.readline()))
    
    ret = make_numbers(card, select_till, selected)
    ret = set(ret)
    print(f"{len(ret)}")