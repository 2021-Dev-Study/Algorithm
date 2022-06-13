if __name__ == "__main__":
    N = int(input())
    T = []
    P = []
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    
    dp = [0]*(N+1)
    for i in range(N-1, -1, -1): # 역순으로 진행
        if T[i] + i > N: # 일을 마무리한 시점이 퇴사 이후인 경우
            dp[i] = dp[i+1]
        else:
            dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    
    print(dp[0])
