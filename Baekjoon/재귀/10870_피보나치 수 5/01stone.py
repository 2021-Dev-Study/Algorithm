# 10870 : 피보나치 수 5


# 재귀 이용
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))


'''
# dp 이용
n = int(input())
dp = [0] * 50
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    # print(i)
    dp[i] = dp[i-2] + dp[i-1]

# print(dp)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 0, 0, ...
print(dp[n])
'''