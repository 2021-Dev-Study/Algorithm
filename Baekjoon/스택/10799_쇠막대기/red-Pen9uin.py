# 작성자: red-Pen9uin
# Data structure: stack
# 23253: 자료구조는 정말 최고야
# 수행 결과: 57020 KB / 412 ms
"""
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다.
괄호 문자의 개수는 최대 100,000이다.

잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.

"""
import sys

""" 풀이 진행중 """
def get_pieces(sticks:str) ->None:
    stick = list()
    is_lazer = False
    result = 0
    cnt = -1

    for i in sticks:
        if i == '(':
            # temp += 1
            stick.append('(')
        else: # if i == ')':
            # if stick.pop
            stick.pop()
            # result += temp
            result += len(stick)
        
    print(f"{result}")
    return


if __name__ == "__main__":
    sticks = sys.stdin.readline().rstrip('\n')
    get_pieces(sticks)

