# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 13305_주유소

"""
https://www.acmicpc.net/problem/13305
"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################


def solution(citys, road_len, oil_price):
    roads = citys - 1
    total_price = 0
    oil_per_killo = oil_price[0]

    for i in range(roads):
        if oil_per_killo > oil_price[i]:
            oil_per_killo = oil_price[i]
        total_price += oil_per_killo * road_len[i]

    return total_price

if __name__ == "__main__":
    citys = int(sys.stdin.readline())
    road_len = list(map(int, sys.stdin.readline().split()))
    oil_price = list(map(int, sys.stdin.readline().split()))

    # citys = 4
    # road_len = [2, 3, 1]
    # oil_price = [5, 2, 4, 1]

    print(solution(citys, road_len, oil_price))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""