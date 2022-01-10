# 문제 번호 10828 스택 

import sys
stk =[]

N = int(sys.stdin.readline())

for _ in range(N):
    menu = sys.stdin.readline().split()
    
    if menu[0] == "push" :
        stk.append(menu[1]) # 2번째 index에 있는 값 삽입
    
    elif menu[0] == "pop" :
        if len(stk) == 0:
            print(-1)
        else :
            print(stk.pop())
            
    elif menu[0] == "size" :
        print(len(stk))
        
    elif menu[0] == "empty" :
        if len(stk) == 0:
            print(1)
        else :
            print(0)
            
    elif menu[0] == "top" :
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1]) 