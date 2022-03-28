N = int(input())
# cards = []
# for _ in range(N) :
#     cards.append(int(input()))
# s = [0]*N
# cards.sort()
# s[0] = cards[0]
# s[1] = cards[1]
# for i in range(2,N):
#     s[i] = cards[i] + sum(s[:i]) + sum(s[:i])
# print(s[N-1])

# 문제 카테고리 : 우선순위 큐
h = []
import heapq
for i in range(N) :
    cards = int(input())
    heapq.heappush(h, cards)
result = 0
while len(h) >= 2 : # 최소 2개 뽑아야함
    a = heapq.heappop(h) # 10 - 30(10+20했던 것)
    b = heapq.heappop(h) # 20 - 40
    s = a+b
    result += s # +30 -> +70
    heapq.heappush(h, s) # 30
print(result)
