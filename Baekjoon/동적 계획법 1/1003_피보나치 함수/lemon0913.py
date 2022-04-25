if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())

        d = [[0,0] for _ in range(41)] # DP 테이블

        d[0] = [1,0]  # d[i]의 0번째 원소는 d[i]를 호출했을 때 0이 출력되는 횟수
        d[1] = [0,1]  # d[i]의 1번째 원소는 d[i]를 호출했을 때 1이 출력되는 횟수

        # d[i]에서 0을 출력하는 횟수는 d[i-1], d[i-2]에서 0을 출력한 횟수의 합
        # d[i]에서 1을 출력하는 횟수는 d[i-1], d[i-2]에서 1을 출력한 횟수의 합
        for i in range(2, N+1):
            d[i][0] = d[i-1][0]+d[i-2][0]
            d[i][1] = d[i-1][1]+d[i-2][1]
        

        print(d[N][0], d[N][1])

