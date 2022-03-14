# 작성자: red-Pen9uin
# 1회차 작성: 2022-03-06
# Classification: greedy algorithm

"""########### for time & memory trace ###########"""
# import sys
# sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
# import mytracker
##################################################

word = sys.stdin.readline().rstrip('\n')
num = int(word[0])

for i in range(1, len(word)):
    data = int(word[i])
    if num <= 1 or data <= 1: # 0, 1
        num += data
    else: # int(i) is bigger than 1
        num *= data

print(num)

##################################################
# mytracker.finish()
"""########### for time & memory trace ###########"""