# 큐 (실버 3까지)
# 10845_큐

import sys
from collections import deque

if __name__ == "__main__":
    N = int(input())
    queue = deque([])

    for _ in range(N):
        com = sys.stdin.readline().split()

        if com[0] == 'push':
            queue.append(com[1])

        elif com[0] == 'pop':
            if not queue:
                print(-1)
            else:
                print(queue.popleft())

        elif com[0] == 'size':
            print(len(queue))
        
        elif com[0] == 'empty':
            if not queue:
                print(1)
            else:
                print(0)

        elif com[0] == 'front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
        
        else:
            if not queue:
                print(-1)
            else:
                print(queue[-1])
