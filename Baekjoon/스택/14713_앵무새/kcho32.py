import sys


n = int(sys.stdin.readline().rstrip())
strings = []
## ['you', 'see', 'to', 'week', 'luck', 'good', 'next', 'want', 'i']
stack = []

for i in range(n):
    str = sys.stdin.readline().rstrip().split(" ")[::-1]
    strings.append(str)
## [['you', 'see', 'to', 'want', 'i'], ['week', 'next'], ['luck', 'good']]

goal = sys.stdin.readline().rstrip().split(" ")[::-1]
answer = ""


while True:
    count = 0
    x = goal.pop()
    for i in range(n):
        if strings[i]:
            if strings[i][-1] == x:
                stack.append(strings[i].pop())
            else:
                count += 1
        else:
            count += 1
    if count == n:
        answer ="Impossible"
        break
    elif count != n and not goal:
        for i in range(n):
            if not strings[i]:
                answer = "Possible"
            else:
                answer = "Impossible"
        break

print(answer)
