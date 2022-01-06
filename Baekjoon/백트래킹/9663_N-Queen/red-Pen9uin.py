"""
In Progress
"""
# 작성자: red-Pen9uin
# level 14: Backtracking
# 9663: N0Queen
"""
N-Queen 문제는 크기가 N x N인 체스판 위에
퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때,
퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

"""

import sys
import copy
    
def save_queen(num:int, move:list, row:list, col:list):
    now = len(row)+1
    row_now = copy.deepcopy(row)
    col_now = copy.deepcopy(col)

    row_now.append(now)
    for_range = list(range(0, num))
    for_range = [n for n in for_range if not in col_now]

    for c in for_range:
        
if __name__ == "__main__":
    num = int(sys.stdin.readline())
    
