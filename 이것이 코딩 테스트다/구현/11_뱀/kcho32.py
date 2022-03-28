import sys
from collections import deque


# n: 보드 크기
# k: 사과 갯수
# apples: 사과 위치 [[좌표], [좌표], ...]
# l: 명령 갯수
n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for i in range(k)]
l = int(input())

# 방향은 오른쪽으로 가는 것을 기준으로 잡음
direction = 0
moving = [(1, 0), (0, 1), (-1, 0), (0, -1)]
current_time = 0
current = [0, 0]
body = deque([[0, 0]])
loop_break = False

# 사과 놓고 -> 행열 기준이라 [행][열] -> (열, 행)
board ={f'{[i, j]}' : 2 if [j+1, i+1] in apples else 0 for i in range(n) for j in range(n)}
board[f'{current}'] = 1

cmds = [list(map(str, sys.stdin.readline().split())) for i in range(l)]

# 루프는 sys 사용
for cmd in range(l+1):
    if loop_break:
        break
    if cmd != l:
        time, turn = cmds[cmd][0], cmds[cmd][1]
        time = int(time) - current_time
    else:
        time = n
    # 움직임 거리
    for i in range(time):
        current_time += 1
        next_x, next_y = current[0], current[1]
        next_x += moving[direction][0]
        next_y += moving[direction][1]
        
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
            current[0], current[1] = next_x, next_y
        
            if board[f'{current}'] == 0:
                board[f'{current}'] = 1
                body.append([current[0], current[1]]) # 그냥 current를 넣었을 때에는 current값이 바뀔 때마다 리스트 안의 내용도 바뀜
                board[f'{body.popleft()}'] = 0
            elif board[f'{current}'] == 1:
                loop_break = True
                break
            else:
                board[f'{current}'] = 1
                body.append([current[0], current[1]])
        else:
            current[0], current[1] = next_x, next_y
            loop_break = True
            break
        # 테스트 코드
        # for col in range(n):
        #     for row in range(n):
        #         print(board[f'{[row, col]}'], end=" ")
        #     print("")
        # print(f'{current_time}\n')
    # 방향 전환
    if turn == 'D':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4    
    

print(current_time)
