# 11650	: 좌표 정렬하기

n = int(input())

coor = []
for i in range(n):
  [a, b] = map(int, input().split())
  coor.append([a, b])

coor_sort = sorted(coor)
for j in range(n):
  print(coor_sort[j][0], coor_sort[j][1])