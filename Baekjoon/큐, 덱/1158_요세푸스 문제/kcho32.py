from collections import deque

x, y = map(int, input().split(" "))
answer_list = []
# 1 ~ 목표 수까지의 덱 생성
deq = deque(range(1, x + 1))

## 2번째 input -1 만큼 로테이트 후, pop을 통해 두번째 y번째 수를 answer리스트에 넣어준다 -> 반복
for i in range(x):
    deq.rotate(-(y-1))
    answer_list.append(str(deq.popleft()))

print(f'<{", ".join(answer_list)}>')