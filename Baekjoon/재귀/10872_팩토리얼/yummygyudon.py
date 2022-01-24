# N 팩토리얼 (N!) = N*(N-1) 
def Factorial(n) : # 굳이 왜 0! = 1 인가에 대해 깊게 생각하지 않았음..
    if n == 0: # 종료조건
        return 1 # 특이 값인 0!이 됐을 때 1만 반환하게끔 해서 0!일 때를 대비
    return n * Factorial(n-1)
n = int(input())
print(Factorial(n))
