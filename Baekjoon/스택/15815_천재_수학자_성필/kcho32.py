import sys


equation = list(sys.stdin.readline().rstrip()[::-1])
stack = []

while equation:
    x = equation.pop()
    if x in "/*-+":
        if x == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
        elif x == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
        elif x == '*':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
        elif x == '/':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 // num2) ## 정수!!!!!!!!!!!!!
    else:
        stack.append(int(x))

print(stack.pop())    