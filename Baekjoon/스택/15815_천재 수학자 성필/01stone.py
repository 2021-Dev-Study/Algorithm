# 15815	: 천재 수학자 성필 silver_4
'''
우선 주어진 식을 연산자의 우선순위에 따라 괄호로 묶어준다. 
그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다. 
    그다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 a+bc*가 된다. 
    마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.
'''
# 성필이 수학천재는 아닌듯

eq = input().rstrip()
stk = []

for i in eq:
    if i == '+':          # 스택에 넣은 숫자 순서대로 연산자 i 계산
        a = stk.pop()
        b = stk.pop()
        stk.append(a + b)
    elif i == '-':
        a = stk.pop()
        b = stk.pop()
        stk.append(b - a)  # 순서^^...유의^^
    elif i == '*':
        a = stk.pop()
        b = stk.pop()
        stk.append(a * b)
    elif i == '/':
        a = stk.pop()
        b = stk.pop()
        stk.append(b // a)
    else:                  # 여기서 앞에 숫자 전부 스택으로 들어감
        stk.append(int(i))

if len(stk) == 1:
    print(stk[0])
    


