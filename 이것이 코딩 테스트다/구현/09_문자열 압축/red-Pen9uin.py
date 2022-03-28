# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# Classification: Implementation algorithm
# 09_문자열 압축

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def solution(s):
    answer = len(s)
    max_check = len(s)//2 + 1

    if len(s)==1:
        return 1

    for step in range(1, max_check):
        # if len(s)%step != 0:
        #     continue
        result = ""
        prev = s[0:step]
        cnt = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                result += str(cnt) + prev if cnt>=2 else prev
                prev = s[j:j+step]
                cnt = 1
    
        result += str(cnt) + prev if cnt>=2 else prev
        answer = min(answer, len(result))
    
    return answer

        


if __name__ == "__main__":
    s = "aabbaccc"
    # s = "ababcdcdababcdcd"
    # s = "abcabcdede"
    # s = "abcabcabcabcdededededede"
    # s = "xababcdcdababcdcd"

    solution(s)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""