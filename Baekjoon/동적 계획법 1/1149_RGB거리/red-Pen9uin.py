# 작성자: red-Pen9uin
# 작성일: 2022-04-25
# Classification: Dinamic Programming
# 1149_RGB거리

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys
    

if __name__ == "__main__":
    cnt = int(input())
    house = []
    for i in range(cnt):
        house.append(list(map(int, sys.stdin.readline().split())))
    
    # for _ in range():
    #     color = []
    # print(house)
    # ??


    # for i in range(1, cnt):
    #     house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    #     house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    #     house[i][2] = min(house[i-1][1], house[i-1][0]) + house[i][2]
    # print(min(house[cnt-1]))



##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""