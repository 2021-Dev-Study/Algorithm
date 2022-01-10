# 1935 : 후위 표기식2 silver_3
'''
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 
그리고 둘째 줄에는 후위 표기식이 주어진다. 
    (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 
그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 
3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 
그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.
'''
# 숫자는 stk, 연산자 만나면 pop

n = int(input())
eq = input()
operands = [0] * 30
for i in range(n):
    operands[i] = int(input())
stk = []

for i in eq:
    if 'A' <= i <= 'Z':
        stk.append(operands[ord(i) - ord('A')]) # 피연산자는 A부터 Z까지 순차적으로 나오므로 알파벳 번호를 구하면 됨
    else:
        operator_1 = stk.pop()
        operator_2 = stk.pop()

        if i == '+':
            stk.append(operator_1 + operator_2)
        elif i == '-':
            stk.append(operator_2 - operator_1)
        elif i == '*':
            stk.append(operator_1 * operator_2)
        elif i == '/':
            stk.append(operator_2 / operator_1)

print(f'{stk[0]:.2f}')