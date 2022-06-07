# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# 수정일: 2022-06-07
# Classification: Implementation algorithm + 구현
# 13_치킨 배달
# 참고: https://codesyun.tistory.com/185

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""