# 2164 : 카드2
'''
# 시간초과 : pypy3로 해도 시간초과

import sys
input = sys.stdin.readline

n = int(input())

cards = [i for i in range(1, n+1)]

while len(cards) !=1:
    cards.pop(0)
    cards.append(cards.pop(0))

print(cards[0])
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range(1, n+1)])

while len(cards) !=1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])