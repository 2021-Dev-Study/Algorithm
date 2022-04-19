# dp문제를 재귀함수를 사용하여 탑다운 방식으로 푸는 유형
# 메모이제이션 기법을 사용해야 함, 메모이제이션을 사용하지 않으면 재귀 함수를 사용할 때 시간이 기하급수적으로 걸림
# 메모이제이션 = 한 번 구한 결과를 메모리공간에 메모해두고 같은 식을 다시 호출하면 메모해둔 결과를 그대로 가져오는 기법

import sys
if __name__ == "__main__":
    def w(a, b, c):
        # 종료 조건
        if a <= 0 or b <= 0 or c <= 0:
            return 1

        if a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        
        # 이미 계산한 적 있는 문제라면 연산을 다시하지 않고 메모리에 저장된 값을 그대로 반환 
        if dp[a][b][c] :
            return dp[a][b][c]
        

        # 아직 계산한 적 없는 문제라면 연산과정이 필요
        if a<b<c:
            dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
        
    
    # dp 테이블(1부터 20까지)
    dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

    while True:
        a, b, c = map(int, sys.stdin.readline().split())

        # 입력 종료 조건
        if a == -1 and b == -1 and c == -1:
            break

        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')






