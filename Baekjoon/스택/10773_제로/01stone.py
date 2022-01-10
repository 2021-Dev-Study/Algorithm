# 10773	: 제로 silver_4
'''
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 
가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 
'''
import sys
input = sys.stdin.readline # 안넣으면 시간초과 뜸

def sum(n_list): # sum 구현
    sum = 0
    for i in n_list:
        sum += i
    return(sum)

stk = []
for _ in range(int(input())):
    num = int(input())
    
    if num == 0:        # 0일때 바로 직전에 넣은 값 pop
        stk.pop()
    else:
        stk.append(num) # 아니면 스택에 추가

print(sum(stk))
