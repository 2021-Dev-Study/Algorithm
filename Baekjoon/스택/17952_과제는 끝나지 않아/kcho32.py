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
## 위에도 됨


for i in command:
    x = i
# 0이 아니면 새로운 과제
# 과제 들어오자마자 시간 1만큼 작업/
# 작업 후 남은 양이 0이면 done에 push
# 아닌 경우 stack(안끝난 작업)에 push
    if x[0] != 0:
        x.append(x.pop()-1)
        if x[2] == 0:
            done.append(x)
        elif x[2] > 0:
            stack.append(x)
# 0이면 새로운 과제 x
# 안끝나 과제인 stack에서 pop해서 시간 1 깎아줌
# 남은게 0이면 done에 push, 안끝났으면 다시 stack에 push

    elif x[0] == 0:
        if stack:
            prev_hw = stack.pop()
            prev_hw[2] -= 1
            if prev_hw[2] == 0:
                done.append(prev_hw)
            elif prev_hw[2] > 0:
                stack.append(prev_hw)

# 모든 command가 끝나면 done에 있는 작업들의 점수 값을 다 더해준다.
for i in done:
    answer += i[1]

print(answer)