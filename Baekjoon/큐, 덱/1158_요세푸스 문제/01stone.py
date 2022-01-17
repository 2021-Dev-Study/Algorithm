# 1158 : 요세푸스 문제
'''
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
'''
# 찾아봄

from collections import deque

n, k = map(int, input().split())
queue = deque([i+1 for i in range(n)])
stk = []

while queue:
    queue.rotate(-(k-1))
    stk.append(str(queue.popleft()))

print(f'<{", ".join(stk)}>')