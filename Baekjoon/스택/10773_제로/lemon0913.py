# 스택 (실버 3까지)
# 10773_제로

if __name__ == "__main__":
    K = int(input())
    stack = []
    
    #입력받은 수가 0이 아니면 stack에 추가하고
    #입력받은 수가 0이면 pop
    for i in range (K):
        num = int(input())
        if num != 0:
            stack.append(num)
        else:
            stack.pop()
    
    #스택에 저장된 수의 합 구하기
    sum = 0
    for i in stack:
        sum += i
    print(sum)


