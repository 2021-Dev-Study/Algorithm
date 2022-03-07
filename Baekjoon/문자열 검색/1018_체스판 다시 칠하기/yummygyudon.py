import sys
N,M = map(int,sys.stdin.readline().split())
board = [None]*N
repaint = []
for i in range(N):
    board[i] = sys.stdin.readline().rstrip()
# print(board)

# B가 아닌 경우와 W가 아닌 경우에 각 각 1 더해주면 마지막엔 다 최소 1이 남게되지 않을까라는 바보같은 생각을 했는데
# 만약 처음에 "B"가 오는 올바른 체스판이라고 했을 때,
# 처음 (0,0) _ "(h+w) % 2 == 0" 시작 때 W_start = 1이 되고, B_start = 0이 될 것이고
# 앞으로도 짝수일 땐 B가 와야 W_start에만 1이 더해진고 B_start가 0으로 유지된다는 규칙이 생긴다.
# (짝수일 때, W가 오면 B_start에 1이 더해지면서 B로 시작했을 때나 맞는 색깔이니
# 고쳐야하는 색으로 취급되게 된다.

# 다음 순서(0,1) 때는 W가 오는데
# 그땐 else문으로 넘어가서 W_start에 다시 +1이 된다. 여전히 B_start = 0으로 된다.

# 올바른 체스판의 경우 : 둘 중 한 값이 64, 나머지 하나는 0이 되어야한다.

for hs in range(N-7): # 8칸 높이를 8x8규격에 맞게끔 위에서부터 "행 index"
    for ws in range(M-7) : # 8칸 넓이를 8x8규격에 맞게끔 왼쪽에서부터 "열 index"
        W_start = 0
        B_start = 0
        for h in range(hs, hs+8) :
            for w in range(ws, ws+8) :
                if (h+w)%2 == 0 :
                    if board[h][w] != 'B' : B_start += 1
                    # 짝수일 때, W일 경우는  W_start에서 올바른 경우이니
                    # B로 시작한 경우의 입장에선 틀린 블럭이 된다 -> B_start + 1
                    if board[h][w] != 'W' : W_start += 1
                    # 짝수일 때, B일 경우는 B_start에서 올바른 경우이니
                    # W로 시작한 경우의 입장에선 틀린 블럭이 된다 -> W_start + 1

                #홀수의 경우
                else :
                    if board[h][w] != 'B' : W_start += 1
                    if board[h][w] != 'W' : B_start += 1
        # 각 8x8 경우에서
        # Black 시작 / White 시작 하는 각각의 경우의 잘못 칠한 블럭의 갯수들 저장
        repaint.append(min(W_start,B_start))
print(min(repaint))


# 격자무늬로서 보려고 했는데 반례가 너무 많다.
# 1x3 & 3x1씩나눠서 3x3범위만큼씩 검사하고 넘어가려고했지만
# 그 이후 범위를 벗어나면 바로 위에 검사했던 3줄 중 마지막 줄과 비교할 수가 없고
# 중복되서 세어지는 경우가 많음.

# for hs in range(N-7): # 8칸 높이를 8x8규격에 맞게끔 위에서부터 "행 index"
#     for ws in range(M-7) : # 8칸 넓이를 8x8규격에 맞게끔 왼쪽에서부터 "열 index"
#         # 밑에서부터 좌표 계산 시작
#         re = 0
#
#         for h in range(hs+1, hs+8,3): # 2줄씩 보기 위해 +8이 아닌 +6
#             # bottom = set()
#             # right = set()
#             for w in range(ws, ws+7): # ws
#                 # (h,w)에 대해 (h+1,w) 와 (h,w+1)비교
#                 if (board[h][w] != board[h][w+1]) or (board[h][w] != board[h+1][w]):
#                     bottom.add([[h,w]])
#
#                 if board