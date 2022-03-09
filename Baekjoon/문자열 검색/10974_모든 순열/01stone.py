# 10974 : 모든 순열

from itertools import permutations

n = int(input())
n_list = [i for i in range(1, n+1)]
# print(n_list)
n_permutations = list(permutations(n_list, n))

for i in n_permutations:
  for j in i:
    print(j, end=' ')
  print()