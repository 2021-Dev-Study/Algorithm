# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 
#

def factorial(x):
    if x > 0:
        return x * factorial(x-1)
    else:
        return 1

print(factorial(10))

"""
x * factorial(x-1)
= x * (x-1) * facotrial(x-2)
= x * (x-1) * (x-2) * facotrial(x-3) ... * 1

"""
