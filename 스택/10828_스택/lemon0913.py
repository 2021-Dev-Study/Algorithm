# 스택 (실버 3까지)
# 10828_스택

import sys

if __name__ == "__main__":
    N = int(input())
    stack = []

    for i in range (N):
        com = sys.stdin.readline().split()

        # push x : x를 스택에 넣기
        if com[0] == "push":
            stack.append(com[1])
        
        # pop : 스택의 가장 위에 있는 정수를 뺴서 출력
        # 만약 스택이 비었으면 -1을 출력
        elif com[0] == "pop":
            if len(stack) == 0:
                print('-1')
            else:
                print(stack.pop())
        
        # size : 스택에 들어있는 정수의 개수 출력
        elif com[0] == "size":
            print(len(stack))
        
        # empty : 스택이 비었으면 1, 아니면 0을 출력
        elif com[0] == "empty":
            if len(stack) == 0:
                print('1')
            else:
                print(0)
        
        # 스택의 가장 위에 있는 정수를 출력
        # 만약 스택이 비었으면 -1을 출력
        else:
            if len(stack) == 0:
                print('-1')
            else:
                print(stack[-1])

        