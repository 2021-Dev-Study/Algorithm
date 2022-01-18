from collections import deque
N = int(input())
card = deque([i for i in range(1,N+1)])
while len(card) >1 :
    if card:
        p = card.popleft()
        print(p , end=' ')
        card.append(card.popleft())
print(card[0])


