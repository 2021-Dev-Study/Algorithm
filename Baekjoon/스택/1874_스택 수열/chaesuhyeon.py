import sys

n = int(sys.stdin.readline())
arr = []
sign=[]
cnt = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num: # 맨 처음에는 cnt 숫자는 1부터니까  입력 들어온 숫자까지 반복문 돌려가며 리스트에 append해줌 / 그 다음 반복부터는 cnt와 num을 비교해가며 while문 실행 or 미실행 함 
        arr.append(cnt)
        sign.append("+")
        cnt += 1
    if arr[-1] == num:
        arr.pop()
        sign.append("-")
    else:
        sign.append("NO")
        
if "NO" not in sign: # sign리스트에 NO가 없으면 그대로 부호만 출력
    for s in sign:
        print(s)
else:
    print("NO") # NO가 있다면 NO출력

# 시간 228ms


# 처음 풀이. 리스트 arr는 pop이 일어나는 리스트고 stk는 원래 숫자들을 알기위해 append만 해주는 리스트   
# 답은 나오는데 로직이 너무 복잡해서 시간초과 ㅜㅜ.... 그래도 짰다는 것에 의의를 두기로....
import sys

n = int(sys.stdin.readline())
arr = []
stk=[]
sign=[]
for i in range(n):
    num = int(sys.stdin.readline())
    if not arr : # 빈 문자열일 경우 . 즉 처음의 경우 
        for j in range(1,num+1):
            arr.append(j)
            stk.append(j)
            sign.append("+")
        arr.pop() # 첫 숫자를 바로 빼줘야 하므로 pop을 진행 
        sign.append("-")

    elif num not in arr:    
        for k in range(max(stk)+1, num+1):   # 원래 숫자들이 있는 리스트에서 max값을 구하고 그 max+1부터 num까지 리스트에 추가..
            arr.append(k)
            stk.append(k)
            sign.append("+")
        arr.pop() # 추가한 num을 바로 pop해줌 
        sign.append("-")
    elif arr[-1] == num :
        arr.pop()
        sign.append("-")

    else:
        
        sign.append("NO")

if "NO" not in sign:
    for s in sign:
        print(s)
else:
    print("NO")
            
###  찾아본 풀이 ####    #### True / False로 하는 방법도 나중에 써봐야할듯 / true false로 했는데 시간 4184나옴.. 무엇?
n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
