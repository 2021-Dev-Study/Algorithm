# 시작점: (1, 1)
# 오른쪽 아래 좌표: (N, N)
# 움직임 방향: 상하좌우
# 움직임 크기/action: 1칸
# 상하 : position[0]
# 좌우 : position[1]

import sys

n = int(sys.stdin.readline())
cmds = list(sys.stdin.readline().rstrip().split())

position = [1, 1] # 좌표 바꿔줘야하니깐 튜플이 아닌 리스트

for cmd in cmds:
    if cmd == "R" and position[1] < n:
        position[1] += 1
    elif cmd == "L" and position[1] > 1:
        position[1] -= 1
    elif cmd == "U" and position[0] > 1:
        position[0] -= 1
    elif cmd == "D" and position[0] < n:
        position[0] += 1

print(position[0], position[1])


