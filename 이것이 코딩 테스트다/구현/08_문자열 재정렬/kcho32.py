import sys
from collections import deque

str = deque(sorted(sys.stdin.readline().rstrip()))

num = 0

while True:
    if str[0] in "1234567890":
        num += int(str.popleft())
    else:
        break

print("".join(str), num, sep="")
