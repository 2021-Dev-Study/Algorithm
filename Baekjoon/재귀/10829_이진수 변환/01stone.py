# 10829	: 이진수 변환

print(bin(int(input()))[2:])

'''
def binary(n): 
    if n < 2:         # n이 2보다 작을 경우
        return str(n)
    else:             # n을 2로 나눈 몫을 재귀로 변환, n을 2로 나눈 나머지를 이진수로 반환
        return binary(n//2) + binary(n%2)

n = int(input())
print(binary(n))
'''