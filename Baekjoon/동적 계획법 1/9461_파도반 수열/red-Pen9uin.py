# 작성자: red-Pen9uin
# 작성일: 2022-04-25
# Classification: Dinamic Programming
# 9461_파도반 수열

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

# 변의 길이는 A(n) = A(n-2) + A(n-3) 형식의 수열

if __name__ == "__main__":
    cnt = int(input())

    num = [1,1,1] # 기본값 초기화

    def p(x):
        length = len(num)
        if length < x:
            for i in range(length, x+1):
                num.append(num[i-2] + num[i-3])
        # print("%d %d"%(zero[num],one[num]))
        return num[x-1]

    for _ in range(cnt):
        now = int(sys.stdin.readline())
        print(f"{p(now)}")



##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""