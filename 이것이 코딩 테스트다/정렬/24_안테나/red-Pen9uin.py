# 작성자: red-Pen9uin
# 작성일: 2022-03-28
# Classification: sort algorithm
# 24_안테나

"""
https://www.acmicpc.net/problem/18310

N개의 정수가 주어진다.
이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

# def solution(cnt, houses):
#     houses.sort()
#     idx = (cnt+1)//2
#     min_len = sum(houses)
#     ans = cnt
    
#     for i in range(idx, -1, -1):
#         mid = houses[i]
#         len_apart = [ x-mid if x>=mid else mid-x for x in houses ]
#         if min_len>=sum(len_apart):
#             ans = i
#             min_len = sum(len_apart)

    # return houses[ans]

def solution(cnt, houses):
    houses.sort()
    
    idx = (cnt-1)//2
    return houses[idx]

if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    # houses = [0]*cnt
    houses = list(map(int, sys.stdin.readline().split()))
    print(solution(cnt, houses))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""