import sys


n = int(sys.stdin.readline().rstrip())
strings = []
stack = []

for i in range(n):
    str = sys.stdin.readline().rstrip().split(" ")[::-1] #굳이 안해도 되네요
    strings.append(str)
## [['you', 'see', 'to', 'want', 'i'], ['week', 'next'], ['luck', 'good']]

goal = sys.stdin.readline().rstrip().split(" ")[::-1]
## ['you', 'see', 'to', 'week', 'luck', 'good', 'next', 'want', 'i']

answer = ""

while True:
    # count: 앵무새의 필요없는 단어 수
    # goal: 목표 string
    # n: 앵무새 수
    # strings: 앵무새 말들(리스트)
    count = 0
    x = goal.pop()
    # 앵무새별들의 단어(pop)들을 goal.pop()과 비교
    # 필요한 단어가 포함되어 있으면 stack에 저장 후 해당 for loop 종료
    # 포함 안되어 있으면 count + 1
    # for loop 종료 후 count의 수가 앵무새 수와 같으면 아무도 필요한 단어가 없는 거기 때문에
    # while loop 종료 -> Impossible
    for i in range(n):
        if strings[i]:
            if strings[i][-1] == x:
                stack.append(strings[i].pop())
                break
            else:
                count += 1
        else:
            count += 1
    if count == n:
        answer ="Impossible"
        break
    # 앵무새한테 필요한 단어가 있었고 목표 string을 다 채우고 앵무새한테 남은 단어들이 없다면
    # Possible
    # 목표는 채웠지만 앵무새가 할말이 남았다면 Impossible
    elif count != n and not goal:
        for i in range(n):
            if not strings[i]:
                answer = "Possible"
            else:
                answer = "Impossible"
                break
        break

print(answer)
