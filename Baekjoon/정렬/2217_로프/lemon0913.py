# 정렬
# 2217_로프

import sys
if __name__ == "__main__":
    N = int(input())
    lopelist = []
    for i in range(N):
        lopelist.append(int(sys.stdin.readline()))
    
    # 입력받은 lopelist를 오름차순으로 정렬
    lopelist.sort()
    
    # 로프들로 들어올릴 수 있는 물체의 최대 중량 구하기
    # 중량이 가장 작은 로프를 하나씩 줄일 때마다 남은 로프들로 들 수 있는 중량을 result 리스트에 저장
    result = []
    x = 0
    for i in range(N):
        x = lopelist[i] * (N-i)
        result.append(x)

    print(max(result))

