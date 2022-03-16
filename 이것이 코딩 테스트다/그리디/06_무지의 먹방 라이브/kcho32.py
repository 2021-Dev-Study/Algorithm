from collections import Counter
food_times = [3, 1, 2]
k = 5
table = {}

for i in range(len(food_times)):
    table[i+1] = food_times[i]

table = Counter(table)

# if k > len(table):
#     k -= len(table)


print(table)