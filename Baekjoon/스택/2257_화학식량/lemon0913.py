# 스택 (실버 3까지)
# 2257_화학식량

if __name__ == "__main__":
    str = input()
    dic = {
        "H" : 1,
        "C" : 12,
        "O" : 16,
        "(" : "("
    }

    #스택에 화학식 앞에서부터 넣기
    stack = []
    for i in range(len(str)):
        #H, C, O, ( 인 경우 스택에 일단 넣기
        #H, C, O인 경우 질량으로 바꿔서 넣고 (인 경우 (을 넣기
        if str[i] in dic:
            stack.append(dic[str[i]])
    
        #닫는 괄효인 경우 괄호 안의 값을 계산해서 스택에 넣기
        #pop한 값이 여는 괄호일 때까지 계산하기
        elif str[i] == ')':
            count = 0
            while True:
                n = stack.pop()
                if n == "(":
                    break
                count += n
            stack.append(count)

        #숫자인 경우 앞의 숫자와 곱한 값을 스택에 넣기
        else:             
            tmp = int(str[i]) * stack.pop()
            stack.append(tmp)

    #스택에 저장되어 있는 숫자 다 더하기
    sum = 0
    for i in stack:
        sum += i
    print(sum)


    



        




#딕셔너리 활용 : https://wikidocs.net/16