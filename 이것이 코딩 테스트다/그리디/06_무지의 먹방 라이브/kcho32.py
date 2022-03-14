from collections import deque
food_times = [3, 1, 2]
k = 5
table = deque()

for i in range(len(food_times)):
    table.append([i, food_times[i]])

for i in range(k):
    while table[0][1] == 0:
        table.rotate(-1)
    table[0][1] -= 1
    table.rotate(-1)
    print("k: ", i, table)