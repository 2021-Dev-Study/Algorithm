# 정렬 (단계별)
# 2108_통계학

# 최빈값을 구하기 위해 collections의 Counter를 사용
import sys
from collections import Counter
if __name__ == "__main__":
    # 수의 개수 N과 N개의 수 입력 받기
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(sys.stdin.readline()))
    
    # 산술평균 출력
    avg = round(sum(lst)/N)
    print(avg)

    # 중앙값 출력
    lst.sort() # 오름차순으로 정렬
    print(lst[N//2])

    # 최빈값 출력
    cnt = Counter(lst).most_common() # 빈도수 높은 순서대로 dictionary 형태로정렬
    if len(lst) > 1 : # lst의 길이가 1보다 클 때
        if cnt[0][1] == cnt[1][1]: # 최빈값이 여러개면
            print(cnt[1][0]) # 두번째로 작은 최빈값을 출력
        else:
            print(cnt[0][0]) # 최빈값이 하나면 그 값을 출력
    else: # lst의 길이가 1일때는 그냥 그 값을 출력
        print(cnt[0][0])

    # 범위 출력
    print(max(lst)-min(lst))
