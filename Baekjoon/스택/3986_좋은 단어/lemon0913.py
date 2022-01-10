# 스택 (실버 3까지)
# 3986_좋은 단어



# 단어를 스택에 넣는 과정에서 연속으로 A 또는 B가 들어오면 그 2개의 알파벳을 스택에서 지워버리기
# 빈 스택이 만들어진다면 좋은단어이다

if __name__ == "__main__":
    N = int(input())
    count = 0

    #입력받은 단어가 좋은 단어인지 확인하기
    #좋은 단어라면 count를 1씩 증가
    for _ in range(N):
        
        stack = []
        str = input()
        
        for i in range(len(str)):
            # 알파벳을 스택에 넣기
            stack.append(str[i])

            # 스택에 연속으로 같은 알파벳이 들어갔다면 2개의 알파벳을 스택에서 제거하기
            if len(stack) >= 2 :
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
        
        #빈 스택이 만들어졌다면 count를 1 증가하기
        if len(stack) == 0:
            count += 1


    print(count)

