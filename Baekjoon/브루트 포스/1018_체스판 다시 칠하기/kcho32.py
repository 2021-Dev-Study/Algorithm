# 브루트 포스 -> 일일히 비교

## 예전에 풀었을 때
# go = []
# change = {}
# coordinate = input().split(" ")
# for i in range(int(coordinate[0])):
#     row_element = input()
#     go.append(row_element)

## 시작점을 (0, 0)부터 (m-8, n-8)까지의 범위를 가지고 비교
## 시작점이 B인 경우와 W인 경우 둘다 고려해서 결과값 출력
# for j in range(int(coordinate[0])-7):
#     for i in range(int(coordinate[1])-7):
#         change[(i, j)] = 0
#         first = go[j][i]
#         compare = 0
        
#         if first == "B":
#             check = "W"
#             for k in range(8):
#                 for l in range(8):
#                     if k % 2 == 0:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] != check:
#                                 compare += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] == check:
#                                 compare += 1
#                     elif k % 2 == 1:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] == check:
#                                 compare += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] != check:
#                                 compare += 1
        
#             for k in range(8):
#                 for l in range(8):
#                     if k % 2 == 0:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] != first:
#                                 change[(i, j)] += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] == first:
#                                 change[(i, j)] += 1
#                     elif k % 2 == 1:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] == first:
#                                 change[(i, j)] += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] != first:
#                                 change[(i, j)] += 1
#         if first == "W":
#             check = "B"
#             for k in range(8):
#                 for l in range(8):
#                     if k % 2 == 0:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] != check:
#                                 compare += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] == check:
#                                 compare += 1
#                     elif k % 2 == 1:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] == check:
#                                 compare += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] != check:
#                                 compare += 1
        
#             for k in range(8):
#                 for l in range(8):
#                     if k % 2 == 0:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] != first:
#                                 change[(i, j)] += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] == first:
#                                 change[(i, j)] += 1
#                     elif k % 2 == 1:
#                         if l % 2 == 0:
#                             if go[j+k][i+l] == first:
#                                 change[(i, j)] += 1
#                         elif l % 2 == 1:
#                             if go[j+k][i+l] != first:
#                                 change[(i, j)] += 1
#         if compare != 0 and compare < change[(i,j)]:
#             change[(i,j)] = compare

# print(change[min(change, key=change.get)])

import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
go = [list(sys.stdin.readline().rstrip()) for i in range(n)]
min_value = 65 # 8x8 = 64가 max이므로 그보다 1 더 큰 수로 초기화

# m-8까지 포함시키려면 range(m-7)
# 바둑판은 8 x 8 이기 때문에 n-8, m-8까지밖에 시작범위를 가질 수 없음
# 각각의 시작점에서 B와 W로 시작하는 두 개의 경우 모두 고려
# 바둑판의 좌표의 합이 짝수 인 것의 값은 시작점의 것과 같아야 한다. 시작점 : (0, 0)이기 때문에
# 짝수좌표가 W면 W시작은 맞은 것이고 B시작은 틀린것이기 때문에 black_start_fix의 카운트를 하나 올려준다
# 반대의 경우도 같음
# 나온 값 중 가장 낮은 값을 출력 
for y_start in range(n-7):
    for x_start in range(m-7):
        black_start_fix = 0
        white_start_fix = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if (row+col) % 2:
                    if go[y_start + row][x_start + col] == "W":
                        black_start_fix += 1
                    else:
                        white_start_fix += 1
                else:
                    if go[y_start + row][x_start + col] == "W":
                        white_start_fix += 1
                    else:
                        black_start_fix += 1
        if black_start_fix > white_start_fix and white_start_fix < min_value:
            min_value = white_start_fix
        elif black_start_fix <= white_start_fix and black_start_fix < min_value:
            min_value = black_start_fix

print(min_value)
        