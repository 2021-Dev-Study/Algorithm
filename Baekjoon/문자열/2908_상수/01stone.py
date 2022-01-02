# 상수
'''
입력 : 첫째 줄에 두 수 A와 B가 주어진다. 
       두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
출력 : 첫째 줄에 상수의 대답을 출력한다.
'''

'''
trial_1 : 런타임에러
A = int(input())
B = int(input())
A = int(A[::-1]) 
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)
'''

A, B = input().split() # 문자열로 입력받음..아마도?
a = int(A[::-1]) 
b = int(B[::-1])
print(max(a, b))