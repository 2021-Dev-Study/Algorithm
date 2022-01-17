# 큐 (실버 3까지)
# 2164_카드2

from collections import deque

if __name__ == "__main__":
    N = int(input())

    queue = deque(range(1, N+1))

    # 마지막 카드가 남을 때 까지 반복
    for _ in range(N-1):
        queue.popleft()
        queue.rotate(-1)

    print(queue[0])


# 큐의 제일 왼쪽 값을 버리고 큐를 왼쪽으로 한 칸 이동하는 작업을 마지막 카드가 남을 때 까지 하면 됨 