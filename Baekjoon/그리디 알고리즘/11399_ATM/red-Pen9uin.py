# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 11399_ATM

"""
https://www.acmicpc.net/problem/11399
"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################

def solution(n, p):
    p.sort()
    result = 0

    for i in range(0, n):
        result += (n - i) * p[i]
        
    return result

if __name__ == "__main__":
    n = 5
    p = [3,1,4,3,2]

    # n = int(sys.stdin.readline())
    # p = list(map(int, sys.stdin.readline().split()))
    print(solution(n, p))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""