# 작성자: red-Pen9uin
# 작성일: 2022-03-28
# Classification: sort algorithm
# 25_실패율

"""
https://programmers.co.kr/learn/courses/30/lessons/42889

전체 스테이지의 개수 N,
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,

실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록
solution 함수를 완성하라.

"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def solution(N, stages):
    stages.sort()
    
    answer = []
    challenges = {x:0 for x in range(1, N+1)}
    now = stages[0]
    left = len(stages)
    cnt = 0
    
    for stage in stages:
        if stage > N:
            continue
        elif stage == now:
            cnt += 1
        else:
            rate = cnt/left
            challenges[now] = rate
            left -= cnt
            now = stage
            cnt = 1

    if now <= N:
        rate = cnt/left
        challenges[now] = rate

    challenges = sorted(challenges.items() ,key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in challenges]
      
    return answer

if __name__ == "__main__":
    # N = 5
    # stages = [2, 1, 2, 6, 2, 4, 3, 3]
    # # result = [3,4,2,1,5]

    # N = 4
    # stages = [4, 4, 4, 4, 4]
    # # result = [4, 1, 2, 3]

    N = 4
    stages = [5,5,5,5,5]
    print(solution(N, stages))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""