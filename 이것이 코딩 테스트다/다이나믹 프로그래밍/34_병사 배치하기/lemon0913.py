# 가장 긴 증가하는 부분 수열
if __name__ == "__main__":
    N = int(input())
    sol = list(map(int, input().split()))
    sol.reverse()

    dp = [1]*N
    for i in range(1,N):
        for j in range(0,i):
            if sol[i] > sol[j]:
                dp[i] = max(dp[j]+1,dp[i])
                
    
    print(N-max(dp))