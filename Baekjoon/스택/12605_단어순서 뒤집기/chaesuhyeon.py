import sys
N = int(sys.stdin.readline())
stk = []
cnt = 0

for _ in range(N):
    stk = [] # word를 append 하기전 stk 초기화 
    word = sys.stdin.readline().split() # 공백으로 split
    for _ in range(len(word)): # 입력한 문자의 길이 만큼 반복 
        stk.append(word.pop()) # word에서 하나씩 pop해서 stk에 append

    cnt += 1 # case 번호 1번부터 출력하기 위해서 
    print(f'Case #{cnt}: ' , end='') # end 써서 이어서 출력 
    for j in range(len(stk)): # stk에 담겨진 문자열 하나하나 뽑아서 end 써서 이어서 출력 
        print(stk[j], end=' ')
    print() # case 한개의 출력이 끝나면 줄바꿈 


