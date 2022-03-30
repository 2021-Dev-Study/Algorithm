# (r, c): r행 c열 -> for loop시 행 안에 열 loop 있음
# 계획
# 먼저 치킨 집의 위치와 집의 위치 찾고 각각 리스트에 넣기
# 각 치킨집과 모든 집들의 거리를 합산해서 저장 -> 오름차 정렬 후 앞에서 M개를 더해준다
import sys
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
house_list = []
chicken_list = []
distance_list = []
answer = []

def getDistance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

for row in range(n):
    for col in range(n):
        if board[row][col] == 1:
            house_list.append([row, col])
        elif board[row][col] == 2:
            chicken_list.append([row, col])

for chicken in chicken_list:
    tmp_distance = []
    for house in house_list:
        tmp_distance.append(getDistance(house, chicken))
    distance_list.append(tmp_distance)

# chicken_score = {i: 0 for i in range(len(chicken_list))}

# for i in range(len(house_list)):
#     min_distance = 100000000
#     min_chicken = 0
#     for j in range(len(distance_list)):
#         if distance_list[j][i] < min_distance:
#             min_distance = distance_list[j][i]
#             min_chicken = j
#     chicken_score[min_chicken] += 1

# solution_index = sorted(range(len(distance_list)), key=lambda x: (-chicken_score[x], sum(distance_list[x])))

# for i in range(len(house_list)):
#     min_distance = 100000000
#     for index in solution_index[:m]:
#         if distance_list[index][i] < min_distance:
#             min_distance = distance_list[index][i]
#     answer += min_distance

# print(answer)

possible_options = list(combinations(range(len(chicken_list)), m))

for compare_index in possible_options:
    tmp_list = []
    for i in range(len(house_list)):
        min_distance = 1000000000
        for index in compare_index:
            if distance_list[index][i] < min_distance:
                min_distance = distance_list[index][i]
        tmp_list.append(min_distance)
    answer.append(sum(tmp_list))


print(min(answer))