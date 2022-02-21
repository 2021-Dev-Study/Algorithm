# 문자열 검색
# 14501_퇴사

# dp로 풀어야 할 듯
import sys
if __name__ == "__main__":
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, sys.stdin.readline().split())))
    
    dp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        # i번째 날을 선택했을 때 날짜를 초과하면
        if lst[i][0] + i > N:
            dp[i] = dp[i+1]
        # i번째 날을 선택했을 때 날짜를 초과하지 않으면
        # i번재 날을 선택했을 때와 dp[i+1]의 값 중에서 큰 값을 선택
        else:
            dp[i] = max(dp[i+1], lst[i][1]+dp[i+lst[i][0]])

    print(dp[0])


# dp[i]는 i번째 날 까지 일했을 때의 최대값
# 뒤에서 부터 계산
# 1  2  3  4  5  6  7
# -----------------------
# 3  5  1  1  2  4  2
# 10 20 10 20 15 40 200

# 1)먼저 i번째 날을 선택했을 때 날짜를 초과하지 않는지 확인
# 2)날짜를 초과하지 않으면 i번째 날을 선택하는 것 vs dp[i+1]의 값을 비교해서 더 큰 값을 선택