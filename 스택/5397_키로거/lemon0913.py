# 스택 (실버 3까지)
# 5397_키로거

import sys

if __name__ == "__main__":
    N = int(input())

    for _ in range(N):
        
        str = sys.stdin.readline().replace("\n", "")
        stk_l = []
        stk_r = []
        
        
        for i in str:
            # if i == '<' and len(stk_l) !=0:
            #     stk_r.append(stk_l.pop())
            if i == '<':
                if len(stk_l) !=0:
                    stk_r.append(stk_l.pop())
            
            elif i == '>':
                if len(stk_r) !=0:
                    stk_l.append(stk_r.pop())
            
            elif i == '-':
                if len(stk_l) != 0:
                    stk_l.pop()
            
            else:
                stk_l.append(i)
        
        print(''.join(stk_l+list(reversed(stk_r))))



# 입력받은 문자열에서 개행문자를 제거하고 싶다면
# sys.stdin.readline().replace("\n", "")