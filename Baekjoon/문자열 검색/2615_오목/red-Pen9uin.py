# 작성자: red-Pen9uin
# Classification: string search
# 2615_오목
# 수행 결과:  KB /  ms
"""
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

"""
import sys
import itertools
# 진행중...


def solve(board, size_of_board):
    black = 1
    white = 2

    for row in range(size_of_board):
        for col in range(size_of_board):
            if board[row][col] == 0:
                continue
            if board[row][col] == white or board[row][col] == black:
                result = checkIfThereIsWinner(board, size_of_board, row, col, board[row][col])
                if result:
                    exit()
    
def checkIfThereIsWinner(board, size_of_board, row, col, color):
    count_in_row = 0
    count_in_col = 0
    count_in_diag = 0
    found = False
    place_of_X_and_Y = 0

    for now in range(size_of_board):
        if board[now][col] == color:
            if not found:
                found = True
            count_in_col += 1
        else:
            found = False
            count_in_col = 0
    
    found = False
    for now in range(size_of_board):
        if board[row][now] == color:
            if not found:
                found = True
            count_in_row += 1
        else:
            found = False
            count_in_row = 0
        
        


if __name__ == "__main__":
    size_of_board = 19
    board = [0]*size_of_board
    for i in range(0, size_of_board):
        board = list(map(int, sys.stdin.readline().split()))
    
    solve(board, size_of_board)