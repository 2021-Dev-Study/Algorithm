import sys
from collections import deque

case = int(sys.stdin.readline().rstrip())

for i in range(case):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    prior = list(enumerate(map(int, sys.stdin.readline().rstrip().split(" "))))
    count = 0
    deq = deque(prior)
    
    while prior:
        max_p = max(deq, key=lambda x: x[1])

        if deq[0][1] < max_p[1]:
            deq.rotate(-1)
        else:
            if deq[0][0] == m:
                count += 1
                deq.popleft()
                break
            else:
                count += 1
                deq.popleft()

    print(count)
