# 12789	: 도키도키 간식드리미
'''
두근두근, 오키도키, 도끼도끼...?
문제가 너무 길다... 약간 하노이탑 비스무리 어쩌구 한거인듯
수찬이가 잘못된 데이터를 찾고 수원이가 문제를 만들었음
'''

# 진짜 모르겠어서 찾아봄...deque...라고 함...
from collections import deque

n = int(input())
queue = deque(map(int, input().split())) # deque([5, 4, 1, 3, 2])
stack = deque()                          # deque([])
i = 1
while queue:
    if queue and queue[0] == i: # True/False...????? 여기 이해가 안가요...ㅠ
        queue.popleft()
        i += 1
    else:
        stack.append(queue.popleft())
    while stack and stack[-1] == i:
        stack.pop()
        i += 1
        
print("Nice" if not stack else "Sad")





'''
trial...

n = int(input())
students = deque(map(int, input().split()))
stk = []
min_student = 1

# 일단 몇 번 움직일지 모르니까...while...
while students:
    if students[0] == min_student: # 가장 작은 학생이 가장 오른쪽에 있음 걍 빼버리기
        students.pop(0)            # 첫번째 값 제거
        min_student += 1
    else:
        stk.append(students.pop(0)) # 그거 아니면 첫번째 값을 스택에 넣어두기
    
    while stk:
        if stk[-1] == min_student:
            stk.pop()
            min_student += 1
        else:                
            break

if not stk: print('Nice')
else: print('No')
'''