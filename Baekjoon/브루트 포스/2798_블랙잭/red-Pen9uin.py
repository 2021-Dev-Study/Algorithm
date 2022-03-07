# 작성자: red-Pen9uin
# level 11: brute force
# 2798_블랙잭
# 수행 결과: 41484 KB / 168 ms
"""
각 카드에는 양의 정수가 쓰여 있다.
그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
그런 후에 딜러는 숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다.
블랙잭 변형 게임이기 때문에,
플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때,
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

"""

from itertools import combinations

if __name__ == "__main__":
    n, m = map(int,input().split())

    card = list(map(int, input().split()))
    card_set = list(combinations(card, 3))
    total = 0
    for i in card_set:
        if sum(i) <= m:
            total = max(total, sum(i))
    print(total)


# if __name__ == "__main__":
#     N, M = map(int,(input().split()))

#     d = list(map(int, input().split())) # 카드 리스트

#     result = 0
#     Max = 0

#     for i in range(N-2): # 3중 for문을 돌면서 겹치지 않게 범위를 지정
#         for j in range(i+1,N-1):
#             for k in range(j+1,N):
#                 if d[i]+d[j]+d[k] > M: # 3개의 값 더한것이 M보다 크다면 넘어감
#                     continue
#                 else:
#                     result = d[i]+d[j]+d[k]
#                     if Max <= result: # M과 가장 유사한 값은 가장 큰값이기 때문에 비교해서 큰값을 저장
#                         Max = result