import sys


n = int(sys.stdin.readline().rstrip())
for i in range(n):
    left = []
    right = []
    #str = list(sys.stdin.readline().rstrip()[::-1])
    # while str:
    #     x = str.pop()
        
    #     if x == '<' and left:
    #         right.append(left.pop())
    #     elif x == '>' and right:
    #         left.append(right.pop())
    #     elif x == '-' and left:
    #         left.pop()
    #     elif x not in "<>-":
    #         left.append(x)
    #     # print('left:', left)
    #     # print('right:', right)
    # print("".join(left)+"".join(right)[::-1])

    str = list(sys.stdin.readline().rstrip())
    for ch in str:
        if ch == '<' and left:
            right.append(left.pop())
        elif ch == '>' and right:
            left.append(right.pop())
        elif ch == '-' and left:
            left.pop()
        elif ch not in "<>-":
            left.append(ch)
        # print('left:', left)
        # print('right:', right)
    print("".join(left)+"".join(right)[::-1])
