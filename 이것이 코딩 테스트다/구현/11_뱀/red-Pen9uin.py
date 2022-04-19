# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# Classification: Implementation algorithm
# 11_뱀

"""
https://www.acmicpc.net/problem/3190
"""

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys
from collections import deque

"""
풀이중...
"""

def solution(n, points, moves):
    start = [0,0]
    now = start
    snake = deque([0,0])
    for p in points:
        is_apple = check_for_apple(start, p, points)
    return 0

# def check_for_apple(from_p, to_p, points):
#     direction = {'R': [1,0], 'L': [-1,0], 'U':[0,1], 'D':[0,-1]}
#     dx, dr = direction[to_p[1]]
#     for i in range(to_p[0]):
#         from_p[0]


# def check_for_end():
    

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    # board = [[0]*n] * n

    cnt = int(sys.stdin.readline())
    points = [0]*cnt
    for i in range(cnt):
        dx, dy = map(int, sys.stdin.readline().split())
        # board[dx-1][dy-1] = 1
        points[i] = [dx, dy]

    cnt = int(sys.stdin.readline())
    moves = []
    for i in range(cnt):
        t, d = sys.stdin.readline().split()
        t = int(t)
        moves.append([t, d])
    
    # print(board)
    print(points)
    print(moves)

    solution(n, points, moves)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""