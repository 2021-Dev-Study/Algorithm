# 스택 (실버 3까지)
# 4949_균형잡힌 세상

#문자열에 대해서 괄호의 짝이 맞는지 확인하기
#여는 괄호면, 스택에 넣기
#닫는 괄호면, 스택에서 pop한 값이 짝이 맞는 경우에는 여는 괄호를 스택에서 제거하고 스택에서 pop한 값이 짝이 맞지 않는 경우에는 no출력



if __name__ == "__main__":
    while True:
        str = input()
        # .을 입력받으면 반복문 종료
        if str == '.':
            break
        
        else:
            stk = []
            # 괄호의 짝이 맞는지 판단하는 boolean 변수
            b = True
            
            for i in str:
                # 여는 괄호면 스택에 넣기
                if i == '(' or i == '[':
                    stk.append(i)
                
                # 닫는 괄호면
                elif i == ')':
                    # 닫는 괄호를 스택에 가장 먼저 넣게 되거나 스택의 꼭대기값과 닫는 괄호의 짝이 맞지 않으면
                    if len(stk) == 0 or stk[-1] == '[':
                        # 괄호의 짝이 맞는지 판단하는 boolean을 False로 바꾸고 괄호의 짝을 확인하는 과정 그냥 끝내기
                        b = False
                        break
                    # 스택의 꼭대기값과 닫는 괄호의 짝이 맞으면 꼭대기 값을 스택에서 제거하기
                    elif stk[-1] == '(':
                        stk.pop()

                elif i == ']':
                    if len(stk) == 0 or stk[-1] == '(':
                        b = False
                        break
                    elif stk[-1] == '[':
                        stk.pop()
            # 괄호의 짝이 맞는지 판단하는 boolean이 참이고 stack이 비어있는 경우 yes 출력
            # 스택이 비어있는지 확인하는 이유는 스택에 여는 괄호만 들어간 경우를 방지하기 위해 
            if b == True and len(stk) == 0:
                print('yes')
            else:
                print('no')


         