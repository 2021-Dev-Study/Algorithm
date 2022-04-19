# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 11047_동전 0

"""
https://www.acmicpc.net/problem/11047
"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def solution(num, target, coins):
    cnt = 0
    coins.sort(reverse=True)
    
    for i in range(num):
        if (target/coins[i]) >= 1:
            coin_cnt = (target//coins[i])
            target -= coin_cnt*coins[i]
            cnt += coin_cnt
    return cnt

if __name__ == "__main__":
    num, target = map(int, sys.stdin.readline().split())
    coins = [0]*num
    for i in range(num):
        coins[i] = int(sys.stdin.readline())
    
    print(solution(num, target, coins))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""