# 1406 : 에디터 silver_3
'''
L :	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D :	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B :	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	: $라는 문자를 커서 왼쪽에 추가함
'''
# 시간초과 : pypy3사용
# python3에서 sys 사용이 시간이 더 단축됨

import sys
input = sys.stdin.readline

l = list(input().rstrip())
m = int(input())
stk = []

for i in range(m):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'L' and l != []:     # 커서가 맨 앞이 아니라면
        stk.append(l.pop())           # 왼쪽으로 한 칸 옮김 = 스택으로 치워버림
    elif cmd[0] == 'D' and stk != []: # 커서가 맨 뒤가 아니라면
        l.append(stk.pop())           # 오른쪽으로 한 칸 옮김 = 원래있던 곳에 넣어둠
    elif cmd[0] == 'B' and l != []:   # 커서가 맨 앞이 아니라면
        l.pop()                       # 없애버림
    elif cmd[0] == 'P':
        l.append(cmd[1])              # cmd = [p, 넣을 숫자]

# print(l)
# print(stk)
# l + stk역순
print("".join(l + stk[::-1]))
    



'''
abcd > abcd^
3
P x  > abcdx^  > []
L    > abcd^   > [x] 
P y  > abcdy^  > [x]
abcdyx

abc > abc^
9
L   > ab^  > [c]
L   > a^   > [c, b]
L   > ^    > [c, b, a]
L   > ^    > [c, b, a]
L   > ^    > [c, b, a]
P x > x^   > [c, b, a]
L   > ^    > [c, b, a, x]
B   > ^    > [c, b, a, x]
P y > y^   > [c, b, a, x]
yxabc

dmih > dmih^
11
B    > dmi^ > []
B    > dm^  > []
P x  > dmx^ > []
L    > dm^  > [x]
B    > d^   > [x]
B    > ^    > [x]
B    > ^    > [x]
P y  > y^   > [x]
D    > yx^  > []
D    > yx^  > []
P z  > yxz^ > []
yxz
'''