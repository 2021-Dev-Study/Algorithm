from itertools import permutations, combinations, product

n = int(input())
coins = list(map(int, input().split()))

# value_list = []
value_list = set()
for i in range(len(coins)):
  coin_sum = list(combinations(coins, i))
  for j in coin_sum:
    # value_list.append(sum(j))  # 중복은 제거하는게..
    value_list.add(sum(j))
# print(value_list)

for k in range(1, len(value_list) + 1):
  if k not in value_list:
    result = k
    print(result)
    break

if result > len(value_list):
  print(result)