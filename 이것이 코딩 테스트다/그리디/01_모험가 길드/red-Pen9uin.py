# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: Greedy algorithm
# 01_모험가 길드

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################

"""def solve(n, x):
    x.sort()

    x_cnt = x[0]
    group_cnt = 0
    getting_ready = False

    for i in range(n):
        x_cnt -= 1
        getting_ready = True

        if x_cnt==0:
            x_cnt = x[i]
            if getting_ready:
                group_cnt += 1
                getting_ready = False

    print(group_cnt)"""

def solve(n, x):
    x_new = [num for num in x if num <= n]

    x_new.sort()
    n_new = len(x_new)

    variance = list(set(x_new))
    group_cnt = 0

    for i in range(len(variance)):
        n_new -= variance[i]
        if n_new >=0 :
            group_cnt += 1
        else:
            break
    
    print(group_cnt)

""" Basic Solution
def solve(n, x):
    result = 0
    cnt = 0
    for i in x:
        cnt += 1
        if cnt >= i:
            result += 1
            cnt = 0
    print(result)
"""

if __name__ == "__main__":
    # # Test Case 1
    # n = 5
    # x = [2, 3, 1, 2, 2]

    # # Test Case 2
    # n = 5
    # x = [1,1,1,1,1]

    # # Test Case 3
    # n = 5
    # x = [5,5,5,5,5]

    # # Test Case 4
    # n = 5
    # x = [5,5,5,5,6]

    # Test Case 5
    n = 7
    x = [2, 2, 3, 1, 2, 2, 8]

    solve(n, x)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""