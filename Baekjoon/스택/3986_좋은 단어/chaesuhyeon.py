# 괄호문제랑 비슷한 것 같아서 괄호문제 처럼 풀어봄 

import sys
N = int(sys.stdin.readline())

stk = []
cnt = 0 # 좋은 단어 아닌 것 개수 
for _ in range(N): 
    stk = [] # stk 초기화 
    alpha = sys.stdin.readline().rstrip() # 단어 입력 받음 
    for i in alpha:
        if len(stk) == 0: # stk이 빈리스트면 stk에 append해줌  
            stk.append(i)

        else:  # 빈 리스트가 아닐 경우  
            if i == stk[-1]: # i와 stk마지막 문자가 같으면 
                stk.pop() # 마지막 문자를 pop해서 stk에서 제거 해줌
            elif i != stk[-1]: # i와 stk마지막 문자가 다르면 ex) stk = ['A']인데 i = 'B' 일 경우
                stk.append(i) # stk에 추가해줌 
    if len(stk) != 0: # 반복문을 다 돌았을때 stk가 빈문자열이 아니라면 삭제되지않은 문자가 있다는 뜻 (쌍이 맞지않은 문자 존재)
        cnt += 1 # +1 카운트 해줌 
print(N - cnt) # 최종적으로 전체 단어 개수(N)에서 좋은 단어가 아닌 것 개수(cnt)를 빼줌


    
        
 







