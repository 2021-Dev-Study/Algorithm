# ABC*+DE/-
# [1, 2, 3]
# [1, 6]
# [7]
# [7, 4, 5]
# [7, 0.8]
# [6.2]

import sys    
N = int(sys.stdin.readline()) # 피연산자 개수 
arr = list(sys.stdin.readline().rstrip()) # 입력받은 문자열
stk = []
num= []

for i in range(N) :
    num.append(input()) # 숫자 입력 (예제처럼) 해서 num 리스트에 추가 

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(arr)) : # 입력받은 문자열 길이만큼 반복
    if arr[i].isalpha() : # 만약에 문자 한개가 알파벳이라면 
        arr[i] = num[alpha.index(arr[i])] # alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'에서 arr[i](문자)의 index를 찾고 리스트 num에서 index에 맞는 숫자를 반환하여 문자를 숫자로 치환 

for i in arr : # 문자열에서 하나씩 꺼냄 
    if i.isdigit() : # 문자가 숫자로 되어 있다면 
        stk.append(i) # 스택에 추가 

    else: # 문자열이 숫자가 아니라면
        m = float(stk.pop())
        n = float(stk.pop())
        if i == '+' :
            stk.append(n+m)
        elif i == '-' :
            stk.append(n-m)
        elif i == '*' :
            stk.append(n*m)
        elif i == '/' :
            stk.append(n/m)

print("%0.2f" % (stk[0])) # 소숫점 둘째짜리까지 / 최종적으로 stk에는 결과값이 1개있을 것이므로 stk[0]을 소숫점 둘째자리까지 출력 




######### 찾아본 풀이 #########
# ord함수를 사용하여 푸는 방법
# ord(문자) 함수 : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환

N = int(input())
li = list(input())
nums = [int(input()) for _ in range(N)]
output = []
for t in li:
    if t in "+-*/":
        a = output.pop()
        b = output.pop()
        if t == '+':
            output.append(b+a)
        elif t == '-':
            output.append(b-a)
        elif t == '*':
            output.append(b*a)
        elif t == '/':
            output.append(b/a)
    else:
        output.append(nums[ord(t)-ord('A')])  # ord('A') = 65  /  ord('B') = 66
print("%.2f" % (output[0]))







