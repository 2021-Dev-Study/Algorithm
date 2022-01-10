# 스택 (실버 3까지)
# 9012_괄호



import sys

if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        str = list(input())
        stack = []
        b = True

        for i in range(len(str)):
            #여는 괄호인 경우 스택에 추가
            if str[i] == '(':
                stack.append(str[i])
            #닫는 괄호인 경우    
            else:
                #스택의 꼭대기가 여는 괄호가 아니라면
                if len(stack) == 0:
                    b = False
                    break
                #스택의 꼭대기가 여는 괄호라면
                else:
                    stack.pop()
        
        if len(stack) == 0 and b == True:
            print('YES')
        else:
            print('NO')         

