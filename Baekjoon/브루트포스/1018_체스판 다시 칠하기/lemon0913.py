# 브루트포스
# 1018_체스판 다시 칠하기

import sys
if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append(sys.stdin.readline())
    
    result = []
    count = 0
    # 8 * 8로 수정하기
    # x, y는 행, 열에 대해 원래 체스판에서 8*8 범위의 시작점을 가리킨다
    for y in range(N-7):
        for x in range(M-7):
            # 이제 각 정사각형이 제대로 칠해져 있는지 확인하기
            # 시작점의 x, y 좌표의 합이 짝수 -> x,y좌표의 합이 홀수인 곳은 시작점과 다른 색이고 x,y의 좌표의 합이 짝수인 곳은 시작점과 같은 색
            # 시작점의 x, y 좌표의 합이 홀수 -> x,y좌표의 합이 홀수인 곳은 시작점과 같은 색이고 x,y 좌표의 합이 짝수인 곳은 시작점과 다른 색
            first_W = 0
            first_B = 0
            for Y in range(y, y+8):
                for X in range(x, x+8):
                    if (X+Y) % 2 == 0: # 좌표의 x,y합이 짝수라면
                        if board[Y][X] == 'B':
                            first_W += 1
                        else:
                            first_B += 1
                    else: # 좌표의 x,y합이 홀수라면
                        if board[Y][X] == 'W':
                            first_W += 1
                        else:
                            first_B += 1
            
            result.append(first_W)
            result.append(first_B)
    
    result.sort()
    print(result[0])
    