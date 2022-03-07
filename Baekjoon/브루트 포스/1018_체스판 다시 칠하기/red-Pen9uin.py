# 작성자: red-Pen9uin
# level 11: brute force
# 1018_체스판 다시 칠하기
# 수행 결과: 30864 KB / 68 ms
"""
첫 줄에는 전체 사람의 수 N이 주어진다.
그리고 이어지는 N개의 줄에는
각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

여러분은 입력에 나열된 사람의 덩치 등수를 구해서
그 순서대로 첫 줄에 출력해야 한다.

단, 각 덩치 등수는 공백문자로 분리되어야 한다.
"""
# https://bambbang00.tistory.com/43

import sys

if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    board = [None] * N
    for i in range(N):
        board[i] = list(sys.stdin.readline().rstrip('\n`'))

    cnt = []

    for a in range(N-7):
        for b in range(M-7):
            index1 = 0
            index2 = 0

            for i in range(a, a+8):
                for j in range(b, b+8):
                    if (i+j) % 2 == 0:
                        if board[i][j] != 'W':
                            index1 += 1
                        if board[i][j] != 'B':
                            index2 += 1
                    else:
                        if board[i][j] != 'B':
                            index1 += 1
                        if board[i][j] != 'W':
                            index2 += 1
            cnt.append(min(index1, index2))

    print(min(cnt))
