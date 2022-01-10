import sys
stk1 = list(sys.stdin.readline().rstrip())
stk2 = []
M = int(sys.stdin.readline())
for i in range(M):
    menu = sys.stdin.readline().split()
    if menu[0] == "L":
        if stk1 :
            stk2.append(stk1.pop())
        else :
            continue

    elif menu[0] == "D":
        if stk2 :
            stk1.append(stk2.pop())
        else:
            continue
    elif menu[0] == "B":
        if stk1:
            stk1.pop()
        else :
            continue
    elif menu[0] == "P":
        stk1.append(menu[1])

print(''.join(stk1 + list(reversed(stk2))))



# 첫번째 코드 - 시간초과 
# import sys
# s = list(sys.stdin.readline().rstrip())
# M = int(sys.stdin.readline())
# cursor = len(s)
# for _ in range(M):
#     menu = sys.stdin.readline().split()
#     if menu[0] == "L":
#         if cursor == 0:
#             pass
#         elif cursor > 0 :
#             cursor -= 1

#     elif menu[0] == "D":
#         if cursor == len(s):
#             pass
#         else:
#             cursor += 1

#     elif menu[0] == "B":
#         if cursor == 0:
#             pass
#         elif cursor > 0 :
#             del s[cursor-1]
#     elif menu[0] == "P":
#         s.insert(cursor, menu[1])
# for i in s:
#     print(i ,end='')

    







