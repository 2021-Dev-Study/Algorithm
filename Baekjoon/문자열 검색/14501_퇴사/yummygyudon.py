import sys
N = int(sys.stdin.readline())
able = [0]*(N+1) # 7일 이후의 시점에서 0원부터 시작
table = []
for _ in range(N) :
    table.append(list(map(int,sys.stdin.readline().split())))
for i in range(N-1, -1, -1) : # 역순 검사
    if table[i][0] + i > N : # i : 지금까지 쓴날 / table[i][0] : 이번 상담의 소요될 날
        # ex. 7일까지 가능한경우 소요일자 1의 상담을 7번째 날하게 된다면
        # i, 즉 6 + 1 = 7로 가능함 (index 값을 활용)
        able[i] = able[i+1] # 안되는 경우는 처음이였던 0원을 그대로 적용
        # 앞에 계속 복사 (불가능한 경우)

    else : # (지금까지의 날 + 이번 상담 소요일수) 가 N보다 작거나 같다 == 상담할 수 있는 경우
        able[i] = max( able[i+1] , table[i][1] + able[i+table[i][0]])

print(able[0]) # 역순으로 올라오기때문에 able의 첫 값이 끝에서부터 왔을 때의 마지막값