# 작성자: red-Pen9uin
# Data structure: stack
# 12789: 도키도키 간식드리미
# 수행 결과: 30860 KB / 80 ms
"""
사람들은 현재 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능하다.
인규는 번호표 순서대로만 통과할 수 있는 라인을 만들어 두었다.
이 라인과 대기열의 맨 앞 사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간이 있다.

현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다.
승환이를 도와 프로그램을 완성하라.

입력의 첫째 줄에는 현재 승환이의 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)이 주어진다.
다음 줄에는 승환이 앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서가 앞에서부터 뒤 순서로 주어진다.
승환이가 무사히 간식을 받을 수 있으면 "Nice"(따옴표는 제외)를 출력하고
그렇지 않다면 "Sad"(따옴표는 제외)를 출력한다.

"""
import sys

# def get_snack(waiting: list, num: int) ->None:
#     stack = list()
#     now = 1

#     while waiting:
#         if waiting[0] == now:
#             waiting.pop(0)
#             now += 1
#         else:
#             stack.append(waiting.pop(0))
        
#         while stack:
#             if stack[-1] == now:
#                 stack.pop()
#                 now += 1
#             else:
#                 break
    
#     if stack: # stack이 비어있지 않음 == 순서대로 받지 못함
#         print("Sad")
#     else:
#         print("Nice")

def get_snack(waiting: list, num: int) ->None:
    stack = list()
    stack_cnt = -1
    wait_cnt = num-1

    now = 1 # 간식 받을 차례

    # 검사가 끝날 때까지 루프
    while waiting:
    # while now <= num: # 이 조건으로 수행하면 시간 초과가 뜬다...
        if wait_cnt>=0:
            if waiting[0] == now:
                now += 1
            else:
                stack.append(waiting[0])
                stack_cnt += 1
            del waiting[0]
            wait_cnt -= 1
        
        while stack:
            if stack[stack_cnt]==now:
                del stack[stack_cnt]
                now += 1
                stack_cnt -= 1
            else:
                break

    if stack:
        print("Sad")
    else:
        print("Nice")
    return


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    waiting = list(map(int, sys.stdin.readline().split()))
    
    get_snack(waiting, num)