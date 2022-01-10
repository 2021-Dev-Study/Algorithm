import sys
N = int(sys.stdin.readline().rstrip())
stk = []
sum = 0

for _ in range(N):
    hw= list(map(int, sys.stdin.readline().rstrip().split())) # 과제 정보 입력 

    if hw[0] == 1: # 과제가 존재한다면 
        stk.append([hw[1], hw[2]]) # 점수와 시간만 스택에 추가해줘서 2차원 리스트로 만듦
        print("stk : " , stk)

    if stk: # 숫자가 1이든 0이든 과제의 시간은 감소해야하기 때문에 이렇게 작성 / 스택이 존재한다면 ~ 
        stk[-1][1] -= 1 # 시간 1분 감소 
        print("stk time -1 : " , stk)
        if stk[-1][1] == 0: # 시간이 0분이 되면 점수를 추가해주고 스택에서 빼줌 
            sum += stk[-1][0] 
            stk.pop()
            print("stk pop : ", stk)
        else:
           pass
    else:
        pass           
print(sum) # 최종적으로 더해진 점수 출력 
    




            



