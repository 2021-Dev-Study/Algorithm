import sys

N = int(sys.stdin.readline().rstrip()) # 막대기의 수 
stk =[]
num = []
for _ in range(N): # 막대기의 수 만큼 반복
    num.append(int(sys.stdin.readline().rstrip())) # 입력 받은 막대기의 높이를 리스트에 추가 

stk.append(num[-1]) # stk에 젤 오른쪽 막대기 높이 삽입

for i in range(len(num)): # 막대기 개수만큼 반복함
    p = num.pop() # 오른쪽 막대기부터 봐야하므로 pop해서 막대기 높이 비교함
    if p > stk[-1]: # pop한 막대기가 stk에 추가된 막대기보다 높은 높이라면 
        stk.append(p) # stk에 추가해줌 
print(len(stk)) # 스택의 길이 (막대기의 개수)

    


    







