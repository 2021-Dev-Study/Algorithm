# 큐 (실버 3까지)
# 1966_프린터 큐

import sys
from collections import deque

if __name__ == "__main__" :
    X = int(input())
    
    
    for _ in range(X):
        N, M = list(map(int, sys.stdin.readline().split()))
        imp = deque(list(map(int, sys.stdin.readline().split())))
        index = deque(list(range(N)))

        count = 1 # M이 몇번째로 인쇄되는지 세기 위한 변수
        Max = max(imp)
 
        while True:
            if imp[0] == Max:
                if index[0] == M:
                    break
                else:
                    imp.popleft()
                    index.popleft()
                    count += 1 # 인쇄 한 번 했으니 count 증가
                    Max = max(imp) # 최대값을 꺼내 버렸기때문에 갱신 필요

            else:
                imp.rotate(-1)
                index.rotate(-1)

        print(count)

# M번째 문서가 언제 인쇄될 지 궁금하다 -> M번째 문서가 중요도가 최대면서 맨 앞에 있는 경우가 언제 인지 궁금하다
# 3가지 경우로 나눠서 생각할 수 있음
# 1)맨 앞에 있는 값의 중요도가 최대가 아니면 얘는 일단 인쇄할 수 없음 -> 뒤로 보내버림
# 2)맨 앞에 있는 값이 중요도가 가장 클 경우
# 2-1) 맨 앞 값의 인덱스가 M이 아니면 꺼내서 인쇄하기
# 2-2) 맨 앞 값의 인덱스가 M이면 종료
