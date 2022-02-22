# 아...브루트포스고 뭐고...
# 무식하게 닥조건문으로 해결했습니다.
sentence = list(str(input()))
ls = []
state = False
length = len(sentence)
cnt = 0
for i in sentence :
    # if i =="<" :
    #     state = True
    #     print(i,end='')
    #     continue
    # elif i ==">" :
    #     state = False
    #     print(i,end='')
    #     continue
    if i == "<" : # 여는 괄호일 때, 기존 ls안에 문자가 있으면 먼저 처리
        # " "이나 ">" 때 이미 ls를 초기화하고
        # 특히 ">"때는 state도 변환하기 때문에 잘못된 reversed는 발생하지 않는다.
        if len(ls) > 0 :
            print(f"{''.join(reversed(ls))}{i}", end='') # i를 출력하기 때문에 append 필요 X
            ls = [] # 초기화 필수
        else : # 모두 처리하고 새로운 여는 괄호일때는
            # 우선 출력하기 위해 append
            ls.append(i)
        state = True # 괄호 내부 단어의 순서 방해 못받게 state로 구분
        cnt+=1
        continue
    elif i == ">" :
        print(f"{''.join(ls)}{i}",end='') # 앞서 나왔던 < 부터의 모든 ls 내 문자를 출력
        state = False # state 변환으로 다시 역순 모드로 전환
        ls =[] # 초기화
        cnt += 1
        continue
    elif i == " " :
        if state == True : # 괄호 내부 공백일 경우 "끝나는 경우"가 아니기 때문에 append
            ls.append(i)
        elif state == False : # 괄호 내부가 아닌 경우 "연속 단어 분리 구분자" 이기 때문에
            print(f"{''.join(reversed(ls))}{i}", end='') # "역순문자열 "를 출력
            ls = [] # 초기화
        cnt += 1
        continue
    else : # 일반 문자 (숫자,영문 등) 일 경우
        ls.append(i)
        cnt += 1
    if cnt == length : # 마지막 반복의 경우
        # 마지막이 일반 문자라면
        # 일반 문자의 경우인 else문에는 print문이 없기 때문에 마지막 ls가 출력 안되는 경우 발생
        print(f"{''.join(reversed(ls))}")


