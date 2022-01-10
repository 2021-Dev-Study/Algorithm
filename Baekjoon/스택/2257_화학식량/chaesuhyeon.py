import sys
ch = list(sys.stdin.readline().rstrip())

c = { "H" : 1, "C" : 12, "O" : 16 }

stk=[]

for i in ch:
    if i in c:
        stk.append(c[i]) # 문자 i가 딕셔너리 c에 포함되어 있다면, i의 value값을 stk에 append 
    elif i == "(":
        stk.append(i)
    elif i == ")": # ")"가 나오면 "("가 나올때까지 pop해서 그 숫자들의 누적합을 구해서 stk에 append (15~23행)
        add = 0
        while True:
            a = stk.pop()
            if a == "(": 
                break
            add += a
        if add == 0:
            continue
        else:
            stk.append(add)
    else: # 숫자면 
        num = stk.pop() # 문자지만 , 숫자가 나오면 stk의 최근 데이터를 pop해서 그 숫자와 곱해줌 
        add = num * int(i) # i는 보기에는 숫자지만 문자이므로 int로 바꿔줌
        stk.append(add) # 합을 stk에 append해줌 
print(sum(stk)) # stk의 합을 계산 











