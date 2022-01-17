# 큐 (실버 3까지)
# 2161_카드1

from collections import deque

if __name__ == "__main__":
    N = int(input())

    queue = deque(range(1, N+1))
    result = []

    # 카드가 없어질 때 까지 반복
    for _ in range(N):
        result.append(queue.popleft())
        queue.rotate(-1)

    print(result[0], end='')
    for i in range(1, N):
        print(f' {result[i]}', end='')


# 큐의 제일 왼쪽 값을 버리고 큐를 왼쪽으로 한 칸 이동하는 작업을 마지막 카드가 남을 때 까지 하면 됨 
# 버린 값은 result 리스트에 넣기