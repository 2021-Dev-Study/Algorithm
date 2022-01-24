# 19947 : 투자의 귀재 배주형
# 진짜 귀재네....나는 마이너스인데....풀기 싫다....


'''
# 뭔가 많이 이상하다...잘못 생각한 듯....
sum = 0
def solution(h, y):
  global sum
  if y > 4:
    sum += round(h * 0.35)
    solution(h, y // 5)
  elif 2<y and y<5:
    sum += round(h * 0.2)
    solution(h, y // 3)
  else:
    sum += round(h * 0.05 * 2)
    print(sum + h)

h, y = map(int, input().split())
solution(h, y)
'''

h, y = map(int, input().split())
dp = [0] * 20
dp[0] = h

for i in range(1, y+1):
    if i >= 5:
        dp[i] = int(max(dp[i-5]*1.35, dp[i-3]*1.2, dp[i-1]*1.05))
    elif i >= 3:
        dp[i] = int(max(dp[i-3]*1.2, dp[i-1]*1.05))
    else:
        dp[i] = int(dp[i-1]*1.05)  # int 처리 안하면 소수점 이상함
    

# print(dp)
print(max(dp))