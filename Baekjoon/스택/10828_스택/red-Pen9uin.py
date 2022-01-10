# 작성자: red-Pen9uin
# Data structure: stack
# 10828: 스택
# 수행 결과: 30864 KB / 76ms
"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""
import sys


def stack_push(stack: list, num: int) ->None:
    stack.append(num)
    return


def stack_pop(stack: list) ->None:
    index = len(stack)
    if index==0 :
        print(-1)
    else :
        print(f"{stack[index-1]}")
        del stack[index-1]
    return


def stack_top(stack: list) ->None:
    index = len(stack)
    if index==0 :
        print(-1)
    else :
        print(f"{stack[index-1]}")
    return


def stack_size(stack: list) ->None:
    print(f"{len(stack)}")
    return


def is_stack_empty(stack: list) ->None:
    if len(stack)>0 :
        print(0)
    else:
        print(1)
    return


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    stack = list()

    for _ in range(0, num):
        word = sys.stdin.readline()

        if word[0] == 'p':
            if word[0:3] == 'pop':
                stack_pop(stack)
            else: # elif word[0:4] == 'push' :
                command, num = word.split()
                num = int(num)
                stack_push(stack, num)
        
        elif word[0] == 't':
            stack_top(stack)

        elif word[0] == 'e':
            is_stack_empty(stack)

        elif word[0] == 's':
            stack_size(stack)
