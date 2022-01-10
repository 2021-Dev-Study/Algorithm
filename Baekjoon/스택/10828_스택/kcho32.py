import sys


n = int(sys.stdin.readline().rstrip())
stack = []
answer = []

for i in range(n):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "top":
        print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print("-1")
    