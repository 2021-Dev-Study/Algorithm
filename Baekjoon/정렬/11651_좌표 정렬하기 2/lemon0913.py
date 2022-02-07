# 정렬 (단계별)
# 11651_좌표 정렬하기 2

import sys
if __name__ == "__main__":
    N = int(input())
    lst = [0]*N
    for i in range(N):
        lst[i] = list(map(int, sys.stdin.readline().split()))
        lst[i][0], lst[i][1] = lst[i][1], lst[i][0] # x좌표와 y좌표 위치 바꾸기

    lst.sort() # y좌표 오름차순으로 정렬

    for i in range(N):
        print(lst[i][1], lst[i][0]) # y좌표, x좌표 뒤집어서 출력
     


    