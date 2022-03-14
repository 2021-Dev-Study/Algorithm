from itertools import permutations, combinations, product

n, m = map(int, input().split())
balls = list(map(int, input().split()))
result = list(combinations(balls, 2))

cnt = 0
for i in range(1, m+1):
  if balls.count(i) > 1:
    cnt += result.count((i,i))

print(len(result) - cnt)