# 1874 : 스택 수열 silver_3
'''
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

hint) 1부터 n까지에 수에 대해 차례로 
[push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 
연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
4      []              > []
  push [1]             > []
  push [1, 2]          > []
  push [1, 2, 3]       > []
  push [1, 2, 3, 4]    > []
  pop  [1, 2, 3]       > [4]
3 pop  [1, 2]          > [4, 3]
6 push [1, 2, 5]       > [4, 3]
  push [1, 2, 5, 6]    > [4, 3]
8 pop  [1, 2, 5]       > [4, 3, 6]
  push [1, 2, 5, 7]    > [4, 3, 6]
  push [1, 2, 5, 7, 8] > [4, 3, 6]
7 pop  [1, 2, 5, 7]    > [4, 3, 6, 8]
5 pop  [1, 2, 5]       > [4, 3, 6, 8, 7]
2 pop  [1, 2]          > [4, 3, 6, 8, 7, 5]
1 pop  [1]             > [4, 3, 6, 8, 7, 5, 2]
  pop  []              > [4, 3, 6, 8, 7, 5, 2, 1]
'''
import sys
input = sys.stdin.readline

n = int(input())
stk = []
operators = []
cnt = 0
x = True

for i in range(n):
    num = int(input())
    
    # while i <= num: # 무한루프 돌고있음...안됨...
    while cnt < num: 
        cnt += 1        # 일단 4까지는 넣음
        stk.append(cnt)
        operators.append('+')
    
    if stk[-1] == num:
        stk.pop()
        operators.append('-')
    else:               # 수열이 불가능한 경우
        x = False 
        break         

if x == False: # len(stk) != n 으로 하면 No...
    print('NO') # 이거 NO 대문자...왜 틀리나 했네....
else:
    for j in operators:
        print(j)
