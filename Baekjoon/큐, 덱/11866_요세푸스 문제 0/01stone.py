# 11866 : 요세푸스 문제 0 
# 1158과 동일

from collections import deque

n, k = map(int,input().split()) 
q = deque([i+1 for i in range(n)])
stk = []

while q:
    q.rotate(-(k-1))           
    stk.append(str(q.popleft()))

print(f'<{", ".join(stk)}>')