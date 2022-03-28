# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# Classification: Implementation algorithm
# 07_럭키 스트레이트

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def solution(n):
    check = len(n)%2
    if check > 0:
        print("ERROR")
        return -1
    
    check = len(n)//2
    sum_left = 0
    sum_right = 0

    for i in range(0, check):
        sum_left += int(n[i])
        sum_right += int(n[-i-1])
        # print(sum_left,sum_right)
    
    if sum_left == sum_right:
        print("LUCKY")
    else:
        print("READY")


if __name__ == "__main__":
    # n = '123402'

    n = '7755'

    # n = sys.stdin.readline().rstrip('\n')
    solution(n)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""