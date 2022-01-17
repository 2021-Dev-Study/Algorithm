from collections import deque

x, y = map(int, input().split(" "))
answer_list = []
deq = deque(range(1, x + 1))

for i in range(x-1):
    deq.rotate(-(y-1))
    answer_list.append(str(deq.popleft()))
answer_list.append(str(deq.popleft()))

print(f'<{", ".join(answer_list)}>')