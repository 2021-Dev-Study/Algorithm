# 작성자: red-Pen9uin
# 작성일: 2022-04-25
# Classification: Dinamic Programming
# 1904_01타일

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

if __name__ == "__main__":
    num = int(input())
    dp = [0 for _ in range(num//2+1)]
    print(dp)
    
    for i in range(len(dp)):
        if i==0:
            dp[i] = 1
        else:
            temp = num - i
            # 팩토리얼로 계산..하나?

    



##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""

"""
------ 6자리 수 (n자리 수)
00 * 0 -> 1 (1)
00 * 1 -> 5 (n-1)
00 * 2 -> 4 (n-2)
...
00 * n/
"""
