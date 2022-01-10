# 스택 (실버 3까지)
# 15815_천재 수학자 성필

if __name__ == "__main__":
    math = input()
    stack = []

    # 수식을 앞에서부터 스택에 넣기
    # 스택에 넣는 과정에서 연산자를 만나면 앞의 숫자 2개를 꺼내서 계산한 뒤 다시 스택에 넣기
    for i in math:
        # 숫자인 경우 스택에 넣기
        if '0' <= i <= '9':
            stack.append(i)
        
        # 연산자인 경우 두 숫자를 꺼내서 연산하고 스택에 넣기
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())

            if i == "+":
                stack.append(num2+num1)
            
            elif i == "-":
                stack.append(num2-num1)
            
            elif i == "*":
                stack.append(num2*num1)
            else:
                # stack.append(num2/num1) -> 중간 연산 결과가 모두 정수라고 했으므로 그냥 나누기 연산이 아니라 몪을 구하는 연산이다
                stack.append(num2//num1)
        
        
    print(stack[0])
        

# 연산 결과, 나누기 한 값중에서 소수점 아래 값은 버리고 싶다면
# 몫을 구하는 연산자인 //을 사용하기