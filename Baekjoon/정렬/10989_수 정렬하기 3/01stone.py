# 10989 : 수 정렬하기 3
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 10001

for _ in range(n):
    dp[int(input())] += 1

# print(dp)  # [0, 2, 2, 2, 1, 2, 0, 1, 0, 0, 0, 0, 0, ...

for i in range(len(dp)):
    if dp[i] != 0:
        for j in range(dp[i]):
            print(i)