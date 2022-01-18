import sys
n = int(sys.stdin.readline().rstrip())
# 이 문제도 10845 큐 문제랑 동일한데 입력값의 범위가 2,000,000으로 증가한 문제
# 자세한 풀이는 10845 큐 풀이 참고

# 시간 2624ms 레전드... 메모리 92204kb 레전드 그자체...
# 18258문제에선 오히려 10845문제에서 시간 작게 나온 풀이가 더 오래걸렸고 시간 잡아먹은 deque모듈 사용한게 짧게 걸림

# front = back = 0
# no = 0
# deque = []
# for _ in range(n) :
#     o = sys.stdin.readline().rstrip().split()
#     if len(o) > 1:
#         num = int(o[1])
#         deque.append(num)
#         no += 1
#         back += 1
#     else :
#         if o[0] == 'size':
#             print(no)
#         elif o[0] == 'empty':
#             if no <= 0 : print(1)
#             else : print(0)
#         elif o[0] == 'front':
#             if no <= 0 : print(-1)
#             else : print(deque[front])
#         elif o[0] == 'back':
#             if no <= 0 : print(-1)
#             else : print(deque[back-1])
#         elif o[0] == 'pop' :
#             if no <= 0: print(-1)
#             else:
#                 print(deque[front])
#                 front += 1
#                 no -= 1