import sys


answer = []

while True:
    parenthesis = []
    str = list(sys.stdin.readline().rstrip()[::-1])
    if str == ['.']:
        break
    for i in range(len(str)):
        x = str.pop()
        if len(parenthesis) == 0:
            if x in "[(":
                parenthesis.append(x)
            elif x in "])":
                break
        else:
            if x in "[(":
                parenthesis.append(x)
            elif x in ")]":
                if x == ")":
                    if parenthesis[-1] == "(":
                        parenthesis.pop()
                    else:
                        break
                else:
                    if parenthesis[-1] == "[":
                        parenthesis.pop()
                    else:
                        break
    if len(str) == 0 and len(parenthesis) == 0:
        answer.append('yes')
    else:
        answer.append('no')

print("\n".join(answer))