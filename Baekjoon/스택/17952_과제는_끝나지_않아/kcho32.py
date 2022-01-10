import sys


n = int(sys.stdin.readline().rstrip())
command = []
stack = []
done = []
answer = 0
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    command.append(temp)

# command = command[::-1]

# while command:
#     x = command.pop()

#     if x[0] != 0:
#         x.append(x.pop()-1)
#         if x[2] == 0:
#             done.append(x)
#         elif x[2] > 0:
#             stack.append(x)
#     elif x[0] == 0:
#         if stack:
#             prev_hw = stack.pop()
#             prev_hw[2] -= 1
#             if prev_hw[2] == 0:
#                 done.append(prev_hw)
#             elif prev_hw[2] > 0:
#                 stack.append(prev_hw)

# for i in done:
#     answer += i[1]

# print(answer)

for i in command:
    x = i

    if x[0] != 0:
        x.append(x.pop()-1)
        if x[2] == 0:
            done.append(x)
        elif x[2] > 0:
            stack.append(x)
    elif x[0] == 0:
        if stack:
            prev_hw = stack.pop()
            prev_hw[2] -= 1
            if prev_hw[2] == 0:
                done.append(prev_hw)
            elif prev_hw[2] > 0:
                stack.append(prev_hw)

for i in done:
    answer += i[1]

print(answer)