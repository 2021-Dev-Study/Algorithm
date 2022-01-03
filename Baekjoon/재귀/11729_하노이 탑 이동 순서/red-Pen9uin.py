# 작성자: red-Pen9uin
# level 10: Recursion
# 11729: 하노이 탑 이동 순서
"""
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다.
각 원판은 반경이 큰 순서대로 쌓여있다.
다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라.
단, 이동 횟수는 최소가 되어야 한다.

"""

import sys

# 원래 작성하던 코드:
# def hanoi_tower(board:int) -> None:
#     board_now = [1]*num
#     hanoi(board, board_now[0], 3)

# def hanoi(board:int, now:int, next: int) -> int:
#     if board==1:
#         return next

#     board_now[board-2] = hanoi(board-1, now, next)
    
def hanoi(n, src, dst):
    """
    구현 방향까지는 이해했으나 도저히 코드에 답이 나지 않아,
    검색을 통해 solution을 찾은 뒤 주석을 달며 이해하는 것으로 대체하였다.
    """
    temp = 6 - src - dst
    if n == 0:
        return
    # 원판의 이동은 n에서 1까지 단계별로 순차적으로 이루어진다
    # 한 단계의 이동은 그 위로 존재하는 모든 원판을 temp로 이동하고,
    hanoi(n - 1, src, temp)
    # 해당하는 단계인 n번째 원판을 src에서 dst로 이동시킨 뒤
    move.append([src, dst])
    # temp에 존재하는 모든 원판을 n번째 원판 위로 옮기는 것에 있다
    hanoi(n - 1, temp, dst)
    # 이 과정을 반복하도록 재귀함수를 구성하면 된다.

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    move = []
    hanoi(num, 1, 3)
    print(len(move))
    print('\n'.join([' '.join(str(i) for i in row) for row in move]))
