# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 04_만들 수 없는 금액

"""########### for time & memory trace ###########"""
# import sys
# sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
# import mytracker
##################################################

def solve(n, data):
    data.sort()
    target = data[0]

    for i in range(1, n):
        if target < data[i]:
            break
        target += data[i]

    print(target+1)
    return target

if __name__ == "__main__":
    n = 5
    data = [3, 2, 1, 1, 9]

    # n = int(sys.stdin.readline())
    # data = list(map(int, sys.stdin.readline().split()))
    solve(n, data)


##################################################
# mytracker.finish()
"""########### for time & memory trace ###########"""