# 문제 해결 아이디어 : cseteram이 받아 적은 문장에서 앵무새가 말한 단어와 겹치는 단어가 있으면 pop함 
# 단어가 다 없어지면 Possible / 다 안없어지면 Impossible

import sys
bird = int(sys.stdin.readline().rstrip())
stk = []

status = True # 상태 체크를 위한 변수 
for _ in range(bird): # 앵무새 수만큼 반복하여 앵무새가 말하는거 리스트에 저장 
    stk.append(sys.stdin.readline().rstrip().split()) # 앵무새가 말한 단어? 문장?  [['i', 'want', 'to', 'see', 'you'], ['next', 'week'], ['good', 'luck']]

word = sys.stdin.readline().split() # cseteram이 받아 적은 문장


while word: # word가 존재하는 동안 
    w = word.pop() # (i want next good luck week to see you) 에서 끝에 것부터 pop
    
    for j in range(bird): # 리스트 길이 만큼 반복 해줌 (0 ~ 2만큼)
        if stk[j]: # stk[j]의 데이터가 존재하면 (처음에 이부분 안써줘서 런타임 오류(index error) 났음 )
            if w == stk[j][-1]: # pop한 값과 2차원 배열 안의 끝에 값이 같으면
                stk[j].pop() # 그 값을 pop
                status = True # pop에 성공했으니 상태 True
                break # 바로 위 반복문 종료 

            else: # pop한 값이 2차원 배열 안의 끝값과 같지 않다면
                status = False # 실패했으니 상태 False
           

    if status == False : # 반복이 끝났는데도 상태가 False이면 제거가 안됐다는 뜻 
        print("Impossible") 
        break # 바로 반복문 종료 (뒤에 더 계산할 필요x)

if status == True : # 모든 반복문이 끝나고 상태가 True 라면 
    print("Possible") # 성공 




    







