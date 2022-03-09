import sys
from collections import deque

case = int(sys.stdin.readline().rstrip())
## enumerate로 값의 index를 포함한 튜플을 만들어서 덱에 넣어주었다.
for i in range(case):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    prior = list(enumerate(map(int, sys.stdin.readline().rstrip().split(" "))))
    count = 0
    deq = deque(prior)
    ## max가 있는 동안 회전 시켜주었고, max값과 같으면 빼(pop, count+1)주는데 원하는 index(m)가 나오면 해당 count를 출력
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
