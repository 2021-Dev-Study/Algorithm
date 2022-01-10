# 4949 : 균형잡힌 세상 silver_4
'''
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 
문자열이 균형을 이루는 조건은 아래와 같다.

- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다. : ()
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다. : []
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 
  즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다. : 공백이 짝수개?

문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
'''
# 문자열은...모르겠음...
# 일단...괄호들만 스택에 넣어보는걸로.
# 짝괄호 있으면 빼버리고 아니면 남겨서...뭐 해봄


while True:
    sentence = input()
    stk = []

    if sentence == '.':  # while문 정지 조건
        break

    for char in sentence:
        
        if (char == '[') or (char == '('): # 시작하는 괄호는 일단 넣음
            stk.append(char)
        
        elif char == ']':               # 닫는 괄호는 빈스택이 아니고 시작하는 짝괄호가 있으면 같이 소거
            if (len(stk) != 0) and (stk[-1]=='['):
                stk.pop()
            else:                    # 빈 스택이고, 짝괄호가 없으면 넣음
                stk.append(']')
                break
        
        elif char == ')':              
            if (len(stk) != 0) and (stk[-1]=='('):
                stk.pop()
            else:                   
                stk.append(')')
                break
    
    if len(stk) == 0:
        print('yes')
    else: 
        print('no')




'''
sentence = list(input())

bracket_s_l = sentence.count('(')
bracket_s_r = sentence.count(')')
bracket_b_l = sentence.count('[')
bracket_b_r = sentence.count(']')

if (bracket_s_l == bracket_s_r) and (bracket_b_l == bracket_b_r):
    print('yes')
else:
    print('no')

# 괄호 순서가 바뀌어도 yes라고 출력됨..
'''