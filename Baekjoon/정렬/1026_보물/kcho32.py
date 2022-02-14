import sys
from collections import deque

n = int(input())

first = list(map(int, sys.stdin.readline().rstrip().split(" ")))
second = list(map(int, sys.stdin.readline().rstrip().split(" ")))

answer = 0

first = deque(sorted(first))
second = deque(sorted(second))

for i in range(n):
    answer += first.popleft() * second.pop()

print(answer)

