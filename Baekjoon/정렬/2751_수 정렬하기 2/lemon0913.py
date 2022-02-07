# 정렬 (단계별)
# 2751_수 정렬하기

# 앞의 문제는 삽입 정렬을 구현해서 풀었으나 이번 문제는 N의 벙위로 인해 삽입정렬로 풀 수 없음(시간초과 남) 
# 따라서 이번에는 더 고급 정렬 방법(병합정렬, 퀵정렬, 힙정렬)을 사용해야 한다.
# 문제에서 일단은 파이썬 내장 함수를 사용하라고 권함..

import sys
if __name__ == "__main__":
    # 수의 개수 N과 N개의 수 입력받기
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(sys.stdin.readline()))

    # 리스트 오름차순으로 정렬하기
    lst.sort()

    # 결과 출력
    for i in range(N):
        print(lst[i])

