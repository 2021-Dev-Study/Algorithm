import sys


str = list(sys.stdin.readline().rstrip()[::-1])
stack = []

while str:
    x = str.pop()

    if stack:
        if x == ')':
            if stack[-1] != '(':
                stack.append(x)
            else:
                stack.pop()
        else:
            stack.append(x)
    else:
        stack.append(x)

print(len(stack))
