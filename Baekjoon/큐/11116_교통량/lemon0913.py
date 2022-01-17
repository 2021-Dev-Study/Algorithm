# 큐 (실버 3까지)
# 11116_교통량

import sys
from collections import deque

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        m = int(sys.stdin.readline())
        left = deque(list(map(int, sys.stdin.readline().split())))
        right = deque(list(map(int, sys.stdin.readline().split())))

        countLeft = 0 # 왼쪽에서 오는 차의 숫자를 출력
        while left:
            if left[0] < right[0]:
                left.remove(left[0]+500)
                right.remove(left[0]+1000)
                right.remove(left[0]+1500)
                left.popleft()
                countLeft += 1
            else:
                right.remove(right[0]+500)
                left.remove(right[0]+1000)
                left.remove(right[0]+1500)
                right.popleft()
        
        print(countLeft)


# 235  451  735  951  2351 2851
# 1235 1351 1451 1735 1851 1951
# 오름차순으로 입력받기 때문에 left와 right 큐에서 제일 왼쪽 값이 작은 쪽에서 차가 오는 것임
# t, t+500, t+1000, t+1500에 해당하는 값을 큐에서 제거하기
# left큐, right큐가 빌 때 까지 위 작업 반복하기