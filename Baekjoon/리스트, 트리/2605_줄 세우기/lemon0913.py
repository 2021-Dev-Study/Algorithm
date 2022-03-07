# 리스트
# 2605_줄 세우기

# insert()함수 사용하기
if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    
    result = []
    for i in range(N):
        result.insert(i-nums[i], i+1)
    
    for i in range(N):
        print(result[i], end=' ')
