# 스택 (실버 3까지)
# 1874_스택 수열

if __name__ == "__main__":
    n = int(input())
    stack = []
    result = []
    count = 1
    b = True

    for i in range(n):
        num = int(input())
        
        #push하는 부분
        # 입력 받은 수를 만날 때 까지 push하기
        while count <= num :
            stack.append(count)
            result.append('+')
            count += 1
        
        #pop하는 부분
        # stack의 꼭대기에 있는 숫자가 입력받은 수와 같다면 pop해서 꺼내기
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else: #stack의 꼭대기에 있는 숫자가 입력받은 수와 다르다면 수열 생성 불가
            b = False
            break

    
    if b == True:
        for i in range(len(result)):
            print(result[i])
    else:
        print('NO')

    


        
