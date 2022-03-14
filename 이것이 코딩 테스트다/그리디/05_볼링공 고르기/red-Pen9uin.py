# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 05_볼링공 고르기

"""########### for time & memory trace ###########"""
# import sys
# sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
# import mytracker
##################################################
import itertools

def solve(n, m, data):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if data[i] != data[j]:
                count += 1
    print(count)
    return count

""" Basic Solution
def solve(n, m, data):
    balls = [0] * m
    for x in data:
        balls[x] += 1
    
    result = 0

    for i in range(0,n):
        n -= balls[i]
        result += balls[i] * n
    
    print(result)
    return result
"""

if __name__ == "__main__":
    # n: num of balls
    # m: heaviest weight
    # data: weight of balls
    # n, m = map(int, sys.stdin.readline().split())
    # data = list(map(int, sys.stdin.readline().split()))

    # n, m = 5, 3
    # data = [1,3,2,3,2]

    n, m = 8, 5
    data = [1,5,4,3,2,4,5,2] 

    solve(n, m, data)


##################################################
# mytracker.finish()
"""########### for time & memory trace ###########"""