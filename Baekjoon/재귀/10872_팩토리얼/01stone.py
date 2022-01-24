# 10872 : 팩토리얼


# 재귀 이용
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))


'''
# dp 이용
n = int(input())
dp = [0] * 20
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    # print(i)
    dp[i] = dp[i-1]*i

# print(dp)  # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(max(dp))
'''


'''
n = int(input())
fac = 1
for i in range(1, n+1):
    fac = fac*i
print(fac)
'''