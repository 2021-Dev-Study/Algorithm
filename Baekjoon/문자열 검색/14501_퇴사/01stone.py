# 14501 : 퇴사
# dp로 풀면 편할 것 같음

n = int(input())
schedule = [list(map(int, input().split())) for i in range(n)]
dp = [0] * (2*n)

for i in range(n-1, -1, -1):  # n-1, n-2, n-3, ... , 2, 1, 0 : 역순
  if i + schedule[i][0] > n:  # 현재 날짜와 필요한 날짜가 n을 넘어가는 경우, 이미 퇴사했기에...
                              # 어차피 0 뿐이라...
    dp[i] = dp[i+1]
  else:                       # n을 넘어가지 않는 경우부터 계산함
                              # 현재날짜 + 누적수익 과 다음날수익 중 큰 것
    dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i+1])

print(dp[0])