# 작성자: red-Pen9uin
# 작성일: 2022-04-25
# Classification: Dinamic Programming
# 1003_피보나치 함수

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys
    

if __name__ == "__main__":
    a = int(input())
 
    zero = [1,0,1]
    one = [0,1,1]
    
    def cal(num):
        length = len(zero)
        if length <= num:
            for i in range(length,num+1):
                zero.append(zero[i-1]+zero[i-2])
                one.append(one[i-1]+one[i-2])
        print("%d %d"%(zero[num],one[num]))
    
    for i in range(a):
        k = int(input())
        cal(k)


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""