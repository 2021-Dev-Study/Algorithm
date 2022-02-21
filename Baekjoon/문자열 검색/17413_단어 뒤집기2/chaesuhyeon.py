import sys
from collections import deque

stk = [] 
q=deque()
result = '' 
state = True 

S = sys.stdin.readline().rstrip()

for i in S:
    if i == "<": 
        while stk:
            result += stk.pop()  
        q.append(i) 
        state = False 
    
    elif i == ">": 
        q.append(i) 
        state = True 
        while q : 
            result += q.popleft()
    
    elif i==' ':
        if state:
            while stk:
                result += stk.pop()
            result += ' '  
        else:
            q.append(i) 
            while q: 
                result += q.popleft() #
    else: 
        if state: 
            stk.append(i) 
        else:
            q.append(i) 
while stk: 
    result += stk.pop()
print(result)