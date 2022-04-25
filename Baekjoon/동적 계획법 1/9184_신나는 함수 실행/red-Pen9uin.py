# 작성자: red-Pen9uin
# 작성일: 2022-04-25
# Classification: Dinamic Programming
# 9184_신나는 함수 실행

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys
    

if __name__ == "__main__":
    MAX_SIZE = 20
    # dp = [[[] for b in range(MAX_SIZE)] for c in range(MAX_SIZE)]

    dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]

    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1

        if a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)

        if dp[a][b][c]:
            return dp[a][b][c]

        # if a < b and b < c, then w(a, b, c) returns:
        #     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        if a < b and b < c:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dp[a][b][c]


        # otherwise it returns:
        #     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dp[a][b][c]


    while True:
        a, b, c = map(int, input().split())
        if a==-1 and b==-1 and c==-1:
            break
        else:
            print(f"w({a}, {b}, {c}) = {w(a,b,c)}")


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""