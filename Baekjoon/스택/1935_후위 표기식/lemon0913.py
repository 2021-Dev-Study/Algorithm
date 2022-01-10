# 스택 (실버 3까지)
# 1935_후위 표기식2

import sys

if __name__ == "__main__":
    #N과 후위표기식 입력받기
    N = int(input())
    str = list(input())
    

    #각 피연산자에 대응하는 값을 입력받기
    alph = [0] * N
    for i in range(N):
        alph[i] = int(input())

    #후위표기식을 stack에 넣어가면서 연산하기
    stack = []
    ptn = 0
    for i in range(len(str)):
        
        # 피연산자인 경우 stack에 넣기 
        if 'A' <= str[i] <= 'Z':
            stack.append(alph[ord(str[i])-ord('A')])

        # 연산자인 경우 연산을 수행한 뒤 연산 결과를 stack에 넣기
        elif str[i] == '+':
            
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2+num1)
            

        elif str[i] == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2*num1)

        elif str[i] == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2-num1)

        elif str[i] == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2/num1)
    
    print("{:.2f}".format(stack[0]))
            

#문자를 아스키코드로 변환 ord()
#아스키코드를 문자로 변환 chr()  

