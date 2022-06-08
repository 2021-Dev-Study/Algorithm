# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# 수정일: 2022-05-30
# Classification: Implementation algorithm
# 12_기둥과 보 설치

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def isValid(answer):
    for x,y,a in answer:
        if a==0:
            if (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer or y==0:
                continue
            else:
                return False
        if a==1:
            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = set()
    for x,y,a,b in build_frame:
        if b==0:
            answer.remove((x,y,a))
            if not isValid(answer):
                answer.add((x,y,a))
        else:
            answer.add((x,y,a))
            if not isValid(answer):
                answer.remove((x,y,a))

    answer = [list(i) for i in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer

if __name__ == "__main__":
    n = 5
    x = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

    # n = 5
    # x = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
    solution(n, x)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""