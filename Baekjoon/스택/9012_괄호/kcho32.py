import sys


n = int(sys.stdin.readline().rstrip())
answer = []

for i in range(n):
    temp = []
    str = list(sys.stdin.readline().rstrip()[::-1])
    
    if len(str) % 2 == 0:
        while str:
            x = str.pop()
            if x == '(':
                temp.append(x)
            elif x == ')':
                if temp:
                    if temp[-1] == '(':
                        temp.pop()
                else:
                    break    
    else:
        answer.append('NO')
        continue
    
    if not str and not temp:
        answer.append('YES')
    else:
        answer.append('NO')
print("\n".join(answer))
