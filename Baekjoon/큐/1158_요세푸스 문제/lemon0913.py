# 큐 (실버 3까지)
# 1158_요세푸스 문제

from collections import deque

if __name__ == "__main__":
    N, K = list(map(int, input().split()))

    queue = deque(range(1, N+1)) # 순열 생성

    result = [] # 요세프 순열을 저장할 리스트

    for _ in range(N):
        queue.rotate((K-1)*(-1))
        result.append(queue.popleft())

    # 요세프 순열 출력
    print(f'<{result[0]}', end='')
    for i in range(1,N):
        print(f', {result[i]}', end='')
    print('>')
    
# 요세프 순열을 구하는 방법은 순열을 K-1씩 왼쪽으로 회전시켜
# 가장 왼쪽 값을 꺼내는 것과 같음