# 2605 : 줄 세우기

n = int(input())
n_idx = list(map(int, input().split()))
answer = []

for i in range(n):
  answer.insert(n_idx[i], i+1)
  # print(i, n_idx[i])

for j in answer[::-1]:
  print(j, end=' ')