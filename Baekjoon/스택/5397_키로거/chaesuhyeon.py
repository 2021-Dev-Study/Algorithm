# 1406 에디터 문제와 같은 방법으로 풀었음  근데 시간 1560ms..
import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    stk1 = []
    stk2=[]
    pwd = list(sys.stdin.readline().rstrip())
    for i in pwd: # 입력받은 문자열이 
        if i.isalpha(): # 알파벳이면 stk1에 append
            stk1.append(i) 
        elif i.isdigit(): # 문자인 숫자면 
            stk1.append(i) # stk1에 append
        elif i == "<": # 왼쪽으로 커서 이동하는 경우 
            if len(stk1) > 0: #  # 왼쪽 스택이 빈 리스트가 아니라면 
                stk2.append(stk1.pop()) # 마지막 문자를  pop 해줘서 두번째 스택으로 이동
            else: # 빈 리스트트면
                continue # 무시하고 위로 올라가 반복 수행 
        elif i == ">": # 오른쪽으로 커서 이동하는 경우 
            if len(stk2) > 0: #스택이 빈 리스트가 아니라면
                stk1.append(stk2.pop()) # # 마지막 문자를  pop 해줘서 두번째 스택으로 이동
            else: # 빈 리스트트면
                continue # 무시하고 위로 올라가 반복 수행 
        elif i == "-": # 백스페이스일 경우 &  stk1이 빈 리스트가 아닌 경우  앞 문자 삭제 
            if len(stk1) > 0:
                stk1.pop()  # 왜 stk1에서 마지막 문자를 빼주냐면 백스페이스는 무조건 문자뒤에 올거라고 가정.. 문자 추가는 첫번째 스택 stk1에서 진행되기 때문에 첫번째 스택에서 pop해줌 
            else:
                continue
    print(''.join(stk1 + list(reversed(stk2))))

    
##################### 내 풀이와 비슷한데 좀 더 간단한 코드 #####################
# 나처럼 빈 리스트인지 확인하려고 if문안에 if - else문을 써주는 것보다 참일 때만 실행하도록 if문 만 써줌 
# 또한 알파벳인지, 숫자인지 판단하지않고 그냥 마지막 else문으로 빼줌 
# 내것보단 조금 더 빨리 처리 1188ms
test_cases = int(input())

for _ in range(test_cases):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop()) 
        elif x=="<":
            if left:
                right.append(left.pop())
        elif x=="-":
            if left:
                left.pop()
        else:
            left.append(x)

    print("".join(left)+"".join(reversed(right)))






