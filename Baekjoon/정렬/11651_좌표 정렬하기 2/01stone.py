# 11651 : 좌표 정렬하기 2

n = int(input())

coor = []
for i in range(n):
  [a, b] = map(int, input().split())
  coor.append([b, a])

coor_sort = sorted(coor)
for j in range(n):
  print(coor_sort[j][1], coor_sort[j][0])