# 작성자: red-Pen9uin
# 작성일: 2022-03-28
# Classification: sort algorithm
# 23_국영수

"""
https://www.acmicpc.net/problem/10825

정렬 조건:
0: 이름 1: 국어 2: 영어 3: 수학
국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

"""

"""########### for time & memory trace ###########"""
import sys
sys.path.append('D:\Dropbox\Github-Repository\TIL\mylib')
import mytracker
##################################################
# import sys

def solution(cnt, students):
    students.sort(key=lambda x: x[0], reverse=False)
    students.sort(key=lambda x: x[3], reverse=True)
    students.sort(key=lambda x: x[2], reverse=False)
    students.sort(key=lambda x: x[1], reverse=True)

    names = [n[0] for n in students]
    return names

if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    students = [None]*cnt

    for i in range(cnt):
        temp = list(sys.stdin.readline().split())
        temp = [temp[0], int(temp[1]), int(temp[2]), int(temp[3])]
        students[i] = temp

    print("\n".join(solution(cnt, students)))


##################################################
mytracker.finish()
"""########### for time & memory trace ###########"""