# 후위표기식2와 같은 방법으로 풀이함 
import sys
num = sys.stdin.readline().rstrip()
stk = []
for i in num:
    if i.isdigit():
        stk.append(int(i))
    else:
        n1 = stk.pop()
        n2 = stk.pop()        
        if i == "*":
            stk.append(n2 * n1)

        elif i == "/":
            stk.append(n2 // n1)  # 문제에서 모든 계산 결과가 정수라고 명시되어 있기 때문에 /가 아닌 //로 써줌 

        elif i == "+":
            stk.append(n2 + n1)

        else:           
            stk.append(n2 - n1)
            
print(stk[0])
    
    







