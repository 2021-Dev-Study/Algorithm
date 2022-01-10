import sys
n = int(sys.stdin.readline())
stk = [0]*n # sum 연산을 위해 0으로 사용
ptr = 0

for _ in range(n) :
    num = int(sys.stdin.readline().rstrip())
    if num == 0 : # 0일 경우에는 직전값을 삭제해줘야함
        ptr -= 1 # 현재 ptr은 다음 값 저장을 위해 비어있는(0) 자리에 있기 때문에 줄여준 후
        stk[ptr] = 0 # 0으로 다시 바꾸기
    else :
        stk[ptr] = num
        ptr += 1
print(sum(stk))
