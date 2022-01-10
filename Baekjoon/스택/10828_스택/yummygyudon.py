import sys
n = int(sys.stdin.readline())
stk = [None]*n
ptr = 0

for _ in range(n) :
    order = sys.stdin.readline().rstrip().split(' ')
    if order[0] == 'push' :
        stk[ptr] = int(order[1])
        ptr += 1
    elif order[0] == 'pop' :
        if ptr == 0 : # 비어있을 경우
            print(-1)
        else :
            ptr -= 1 # ptr 줄이고 (다음에 이 줄여진 값에 push되면서 덮어지기 때문에 없앤 것과 마찬가지)
            print(stk[ptr]) # 줄인 ptr위치의 값(top이였던 값) 출력
    elif order[0] == 'size' :
        print(ptr)
    elif order[0] == 'empty' :
        if ptr == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == 'top' :
        if ptr == 0 :
            print(-1)
        else :
            print(stk[ptr-1]) # ptr은 값 삽입을 위해 값이 없는 공간의 인덱스를 갖고 있기때문에 조회만하기 위해 ptr-1 인덱스의 값을 출력
