# 플레이어는 제한된 시간안에 N장의 카드 중에서 3장의 카드를 골라야함
# 플레이어가 고른 카드의 합은 M이 넘지 않으면서 M과 최대한 가깝게 만들어야함
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오

from itertools import combinations # 중복 허용 x --> combinations
n, m = map(int, input().split()) # 카드의 개수(n) , 기준이 되는 카드의 합(m)이 주어짐
card = list(map(int, input().split()))
m_sum = 0 # max sum을 0으로 초기화 

for i in combinations(card, 3): # 카드 리스트에 있는 요소중 3개 뽑음
    card_sum = sum(i) # 3개의 i에 대한 합
    if m_sum < card_sum <= m : # max sum값이 card sum보다 작고, m(기준이 된는 합)보다 작거나 같으면
        m_sum = card_sum # max_sum에 card_sum 대입

print(m_sum)


# 유투브 보고 참고해서 한 풀이
n, m = map(int, input().split())
card = list(map(int, input().split()))

m_sum = 0

for i in range(len(card)):
    for j in range(i + 1, len(card)):
        for k in range(j + 1, len(card)):
            sum = card[i] + card[j] + card[k]
            if sum <= m:
                m_sum = max(m_sum, sum)
print(m_sum)