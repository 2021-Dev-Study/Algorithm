# 정렬 (단계별)
# 2750_수 정렬하기

import sys

if __name__ == "__main__":
    # 수의 개수와 수를 입력받기
    N = int(input())
    lst = []
    for _ in range (N):
        lst.append(int(sys.stdin.readline()))
    
    # 삽입정렬을 사용
    for i in range(1, len(lst)): # 삽입정렬은 두번째 데이터부터 시작
        for j in range(i, 0, -1): #i부터 제일 앞 데이터까지 비교
            if lst[j-1] > lst[j]: # 만약 자신의 왼쪽 데이터가 자신보다 크면 위치를 바꾸기
                lst[j-1], lst[j] = lst[j], lst[j-1]
            else: # 자신의 왼쪽 데이터가 자신보다 작으면 반복문 탈출
                break
    
    # 정렬된 리스트 출력하기
    for k in range(N):
        print(lst[k])