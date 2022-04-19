# 작성자: red-Pen9uin
# 작성일: 2022-03-14
# Classification: greedy algorithm
# 1541_잃어버린 괄호

"""
https://www.acmicpc.net/problem/1541
"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys
import re

def solution(formula):
    answer = 0
    
    num = re.split('[+|-]', formula)
    oper = re.split('[0-9]*', formula)
    oper = ' '.join(oper).split()

    stack = []
    for _ in range(len(num)):
        # print(num, oper, stack)
        stack.append(int(num.pop()))
        try:
            next = oper.pop()
            if next == '+':
                pass
            else: # next == '-'
                answer -= sum(stack)
                stack = []
        except:
            break

    answer += sum(stack)

    return answer

if __name__ == "__main__":
    formula = sys.stdin.readline().rstrip('\n')
    # formula = "55-50+40"
    # formula = "10+20+30+40"
    # formula = "00009-00009"
    
    print(solution(formula))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""