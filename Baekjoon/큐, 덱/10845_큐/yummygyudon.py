import sys
n = int(sys.stdin.readline().rstrip())
# 모듈 사용하기
# 속도 : 96ms
# from collections import deque
# deque = deque()
# for _ in range(n) :
#     o = sys.stdin.readline().rstrip().split()
#     if len(o) > 1:
#         num = int(o[1])
#         deque.append(num)
#     else :
#         if o[0] == 'size':
#             print(len(deque))
#         elif o[0] == 'empty':
#             if len(deque) == 0 : print(1)
#             else : print(0)
#         elif o[0] == 'front':
#             if len(deque) == 0 : print(-1)
#             else : print(deque[0])
#         elif o[0] == 'back':
#             if len(deque) == 0 : print(-1)
#             else : print(deque[-1])
#         elif o[0] == 'pop' :
#             if len(deque) == 0: print(-1)
#             else:
#                 print(deque[0])
#                 deque.popleft()

# 속도 : 76ms | 모듈 쓴것보다 짧게 걸림 & 메모리 더 적게씀
front = back = 0
no = 0
deque = []
for _ in range(n) :
    o = sys.stdin.readline().rstrip().split()
    if len(o) > 1:
        num = int(o[1])
        deque.append(num)
        no += 1
        back += 1
    else :
        if o[0] == 'size':
            print(no)
        elif o[0] == 'empty':
            if no <= 0 : print(1)
            else : print(0)
        elif o[0] == 'front':
            if no <= 0 : print(-1)
            else : print(deque[front])
        elif o[0] == 'back':
            if no <= 0 : print(-1)
            else : print(deque[back-1])
        elif o[0] == 'pop' :
            if no <= 0: print(-1)
            else:
                print(deque[front])
                front += 1
                no -= 1
