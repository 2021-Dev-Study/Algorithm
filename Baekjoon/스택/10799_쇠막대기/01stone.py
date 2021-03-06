# 10799	: 쇠막대기 silver_3
'''
막대기와 레이저의 배치는 다음 조건을 만족한다.
- 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
    쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
- 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다. 

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.
- 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 
    또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
- 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다. 

()(((()())(())()))(())
*(((**)(*)*))(*) 6
((**))*          3
(*)              1
*                1

(((()(()()))(())()))(()())
(((*(**))(*)*))(**) 7
(((*)*))*           3
((*))               1
(*)                 1
*                   1
'''
# 해설 봄...
# '('는 바로 stack에 append : 쇠막대 시작점
# ')'는 전에 '('가 있다면 stack pop 하고 스택 길이와 쇠막대 수 더하기 : 레이저 시작이므로 자르기
#                 없다면 stack pop 하고 쇠막대 + 1                  : 쇠막대 끝부분

iron = list(input())
stk = []
piece = 0

for i in range(len(iron)):
    if iron[i] == '(':
        stk.append(True)
    else:
        if iron[i-1] == '(':  # 레이저
            stk.pop()
            piece += len(stk) # 레이저로 잘랐으니까 그만큼의 쇠막대가 잘려서 len
        else:                 # 쇠막대
            stk.pop()
            piece += 1        # 연결된 쇠막대가 아니라서 

print(piece)



'''
()(((()())(())()))(()) []        0
(                      [(]  
()                     []        0 
()((((                 [(,(,(,(]
()(((()                [(,(,(]   0+3 = 3
()(((()(               [(,(,(,(]
()(((()()              [(,(,(]   3+3 = 6
()(((()())             [(,(]     6+1 = 7
()(((()())((           [(,(,(,(]
()(((()())(()          [(,(,(]   7+3 = 10
()(((()())(())         [(,(]     10+1 = 11
()(((()())(())(        [(,(,(]
()(((()())(())()       [(,(]     11+2 = 13
()(((()())(())())      [(]       13+1 = 14
()(((()())(())()))     []        14+1 = 15
()(((()())(())()))((   [(,(]
()(((()())(())()))(()  [(]       15+1 = 16
()(((()())(())()))(()) []        16+1 = 17 
'''