# 이중 조건 정렬? x축 정렬 -> 같은 값일 경우 y축 정렬
import sys
N = int(sys.stdin.readline())
# axisX = []
# p = []
# for _ in range(N) :
#     x, y = map(int, sys.stdin.readline().split())
#     axisX.append(x)
#     p.append([x,y])
# # set는 자동으로 오름차순 정렬되어서 나옴.
# X = list(set(axisX))
# result = [None]*N
# for point in p :
#     for x in X :
#         if point[0] == x

points= []
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    # 튜플(tuple)을 활용해서 lambda 식으로 이중 정렬 실행
    points.append((x, y))
    # axisX.append(x)
    # axisY.append(y)


    # dictionary 나 set를 활용하여
    # x좌표를 key값으로 설정하여
    # set()로 자동 정렬 후
    # x key값의 value로 들어가있는 list를 정렬하여 출력하려 하였으나 실패
    # points = {}
    # if x in points.keys():
    #     points[x].append(y)
    # else :
    #     points[x] = [y]
# points = { str(x) : str(y) for x, y in zip(axisX,axisY)}


print(points)
# [(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)]
s_points = sorted(points, key= lambda x : (x[0],x[1]))
# [(1, -1), (1, 1), (2, 2), (3, 3), (3, 4)]
for point in s_points :
    print(f"{point[0]} {point[1]}")

# sorted와 lambda 를 사용해서 그런지 시간은 344ms
# 메모리 : 52420KB
# 헐... 검색해보니까 다들 lambda를 써서 풀긴했네요...허탈


