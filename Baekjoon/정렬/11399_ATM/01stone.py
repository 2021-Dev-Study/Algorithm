# 11399 : ATM
# 누적합이 가장 작은 결과가 나오려면 작은 순서대로

n = int(input())
n_time = list(map(int, input().split()))
n_time.sort(reverse=True)

sum_time = []
for i in range(len(n_time)):
    sum_time.append((i+1) * n_time[i])

print(sum(sum_time))



'''
# 2중 for문으로 누적합

n = int(input())
time = list(map(int, input().split()))

time.sort()
ans = 0

for i in range(n):
  for j in range(i+1):
    ans += time[j]

print(ans)
'''



