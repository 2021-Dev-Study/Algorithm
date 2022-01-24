# 재귀 (단계별 & 실버5)
# 10870_피보나치 수 5

# 피보나치 수 F(N)을 구하는 함수를 재귀로 정의
def F(N):

    if N == 0:
        result = 0
    elif N == 1:
        result = 1
    else: # N >= 2일 때 부터 F(N) = F(N-1) + F(N-2)
        result = F(N-1) + F(N-2)
    
    return result

if __name__ == "__main__":
    n = int(input())
    print(F(n))