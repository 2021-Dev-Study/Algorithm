n, k = map(int, input().split())
n_list = [int(input()) for _ in range(n)]

cnt = 0
for i in reversed(range(n)):
  cnt += k//n_list[i]
  # print(cnt) # 50000 > 10000 > 5000 >>>> 1000(으로 4번 나누고 200 남음)
  k = k%n_list[i]
  # print(k)
print(cnt)