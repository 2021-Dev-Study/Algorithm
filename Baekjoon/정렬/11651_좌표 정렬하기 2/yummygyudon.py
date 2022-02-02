## 11650 좌표정렬하기 풀이방법 완전 동일
# lambda에서 기준을 y축만 설정
import sys
N = int(sys.stdin.readline())
points= []
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    points.append([x, y])
s_points = sorted(points, key= lambda x : (x[1], x[0]))
for point in s_points :
    print(f"{point[0]} {point[1]}")