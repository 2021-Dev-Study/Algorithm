n, m = map(int, input().split())

deck = [list(map(int, input().split())) for i in range(m)]
answer_group = []

for cards in deck:
    min = 10001
    for card in cards:
        if card < min:
            min = card
    answer_group.append(min)

print(max(answer_group))