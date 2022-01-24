# 작성자: red-Pen9uin
# level 10: Recursion
# 17478_재귀함수가 뭔가요
# 수행 결과:  KB / 72 ms
"""
제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.
JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자
"""
"""
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
"재귀함수는 자기 자신을 호출하는 함수라네"
라고 답변하였지.
"""

import sys


def what_is_recursion(depth, now):
    recur_story = '''어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'''
    w_is_recur = [
        '''"재귀함수가 뭔가요?"''',
        '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.''',
        '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.''',
        '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."''']
    recur_is = '''"재귀함수는 자기 자신을 호출하는 함수라네"'''
    answered = '''라고 답변하였지.'''

    if now==0:
        print(recur_story)
    
    if now < depth:
        for word in w_is_recur:
            print("____"*now + word)

        what_is_recursion(depth, now+1)

        print("____"*now + answered)
        return

    else: # if now >= depth:
        print("____"*now + w_is_recur[0])
        print("____"*depth + recur_is)
        print("____"*now + answered)
        return

if __name__ == "__main__":
    depth = int(sys.stdin.readline())
    what_is_recursion(depth, 0)