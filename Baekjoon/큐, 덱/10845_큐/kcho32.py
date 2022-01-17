import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
cmd = [sys.stdin.readline().rstrip().split(" ") for i in range(n)]
deq = deque()

for i in cmd:
    if i[0] == "push":
        deq.append(i[1])
    elif i[0] == "front":
        try:
            print(deq[0])
        except:
            print("-1")
    elif i[0] == "back":
        try:
            print(deq[-1])
        except:
            print("-1")
    elif i[0] == "pop":
        try:
            print(deq.popleft())
        except:
            print("-1")
    elif i[0] == "size":
        print(len(deq))
    elif i[0] == "empty":
        if len(deq):
            print("0")
        else:
            print("1")
