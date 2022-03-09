n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0) #뒤에 0을 추가해서 인덱스초과 오류 방지
for i in range(n - 1, -1, -1):
    if t[i] + i > n: #데드라인이 기한을 넘어가는경우
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])   # 둘중에 더 큰값으로 dp[i]값을 갱신하고 최종적으로 dp[0]의 값이 최대가된다
