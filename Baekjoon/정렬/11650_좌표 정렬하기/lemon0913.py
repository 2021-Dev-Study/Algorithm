# 정렬 (단계별)
# 11650_좌표 정렬하기
import sys
if __name__ == "__main__":
    N = int(input())
    lst = [0] * N
    for i in range(N):
        lst[i] = list(map(int, sys.stdin.readline().split()))
    
    lst.sort() # 오름차순으로 정렬(알아서 x좌표가 같으면 y좌표가 증가하는 순서로 정렬해줌)

    for i in range(len(lst)):
        print(lst[i][0], lst[i][1])
    