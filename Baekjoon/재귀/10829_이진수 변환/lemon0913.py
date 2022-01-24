# 재귀 (단계별 & 실버5)
# 10829_이진수 변환

# 이진수로 바꾸는 함수 정의
def binary(n, arr):
    if n >= 1: # n이 1보다 크면 계속 2로 나누기
        arr.append(n%2) 
        n = n//2
        binary(n, arr)     
    
    return list(reversed(arr))


if __name__ == "__main__":
    n = int(input())
    arr = [] # 2로 나눈 나머지를 저장할 리스트
    
    result = binary(n, arr)
    print(''.join(list(map(str, result))))

# 2진수로 바꾸기
# 2 | 53     
# 2 | 26    1
# 2 | 13    0
# 2 | 6     1
# 2 | 3     0
# 2 | 1     1
# 2 | 0     1
#          



# 배열을 뒤집고 싶다면 list(reversed(lst))

