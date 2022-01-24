# 재귀 (단계별 & 실버5)
# 10872_팩토리얼


# 재귀를 사용해 n!을 구하는 함수 정의
def factorial(n):
    if n == 0: # 0!은 1임
        result = 1
    else: # n! = n * (n-1)!
        result = n * factorial(n-1)
    
    return result

if __name__ == "__main__":
    N = int(input())

    print(factorial(N))
