# 문자열 검색
# 1051_숫자 정사각형

import sys
if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [0] * N
    for i in range(N):
        board[i] = sys.stdin.readline()
    
   