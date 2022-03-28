# 작성자: red-Pen9uin
# 작성일: 2022-03-28
# Classification: sort algorithm
# 26_카드 정렬하기

"""
https://www.acmicpc.net/problem/1715

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때,
최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

# def solution(N, num):
#     num.sort()
#     result = 0
#     is_pair = False
#     answer = 0

#     for i in num:
#         result += i
#         if is_pair:
#             answer += result
#             result = answer
#             is_pair = False
#         else:
#             is_pair = True
    
#     return answer

"""
인터넷 검색함!!
"""
import heapq

def solution(N, num):
    if len(num) == 1: #1개일 경우 비교하지 않아도 된다
        return 0
    else:
        answer = 0
        while len(num) > 1: #1개일 경우 비교하지 않아도 된다
            temp_1 = heapq.heappop(num) #제일 작은 덱
            temp_2 = heapq.heappop(num) #두번째로 작은 덱
            answer += temp_1 + temp_2 #현재 비교 횟수를 더해줌
            heapq.heappush(num, temp_1 + temp_2) #더한 덱을 다시 넣어줌
        
        return answer

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    # num = [0]*N
    num = []
    for i in range(N):
        # num[i] = int(sys.stdin.readline())
        heapq.heappush(num, int(sys.stdin.readline()))
    
    print(solution(N, num))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""