# 작성자: red-Pen9uin
# 작성일: 2022-03-21
# Classification: Implementation algorithm
# 08_문자열 재정렬

"""########### for time & memory trace ###########"""
from statistics import variance
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def solution(word):
    alpha = []
    number = []

    for i in word:
        # if i >= "0" and i <= "9":
        #     number.append(int(i))
        # else:
        #     alpha.append(i)
        if i.isalpha():
            alpha.append(i)
        else:
            number.append(int(i))
    
    alpha.sort()

    print("".join(alpha), end="")
    if number:
        print(f"{sum(number)}")

if __name__ == "__main__":
    # word = 'K1KA5CB7'
    # word = 'AJKDLSI412K4JSJ9D'
    word = "AAAAAAAAAAAAAAAAA"

    # word = sys.stdin.readline().rstrip('\n')
    solution(word)

##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""