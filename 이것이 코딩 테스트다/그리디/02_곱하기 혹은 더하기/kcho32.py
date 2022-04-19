'''
입력 조건: 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열
출력 조건: 연산 후 만들어질 수 있는 가장 큰 수
'''
from re import I
import sys
from collections import deque


str = deque(list(map(int, sys.stdin.readline().rstrip())))
answer = str.popleft()

for i in str:
    if answer * i >= answer + i:
        answer *= i
    else:
        answer += i

print(answer)
