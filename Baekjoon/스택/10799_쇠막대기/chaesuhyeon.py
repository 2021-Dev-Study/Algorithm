# 문제 풀이방법을 전혀 생각 못해서 아이디어 참고..
# (가 나오면 stack에 push
# )가 나올 경우 그 전 문자열이 (일 경우 stack에서 pop해주고 스택 크기만큼 result에 더함
# 그 전 문자열이 )일 경우 stack에서 pop하고 result에 1을 증가 시킴

import sys
ps = sys.stdin.readline().rstrip()
stk = []
result = 0

for i in range(len(ps)):
    if ps[i] == "(":
        stk.append("(")
    else: # ")"경우
        if ps[i-1] == "(":
            stk.pop()
            result += len(stk)
        else:
            stk.pop()
            result += 1
print(result)

    







