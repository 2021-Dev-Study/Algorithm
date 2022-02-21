# https://chaewsscode.tistory.com/80 참고 

N , M = map(int, input().split())
chess = [input() for _ in range(N)]
cnt = []

for n in range(N-7): # 시작점
    for m in range(M-7): # 시작점
        W = 0 # W로 시작할 경우 바꿔야할 체스판의 개수
        B = 0 # B로 시작할 경우 바꿔야할 체스판의 개수
        for i in range(n, n+8): # 8x8 만들어줌 , 시작점으로부터 8칸씩 체크
            for j in range(m, m+8): # 8x8 만들어줌 , 시작점으로부터 8칸씩 체크
                # 8*8로 자른 체스판이 W로 시작할 경우에 
                if (i+j) % 2 == 0:  #(i+j) % 2 == 0일 경우 W이어야 함 만약 W가 아니라면 W를 1증가시킴
                    # 마찬가지로 8*8로 자른 체스판이 'B'로 시작할 경우 바꿔야 할 체스판의 개수는 B에 저장
                    if chess[i][j] != 'W':
                        W += 1
                    if chess[i][j] != 'B':
                        B += 1
                else:  # (i+j) % 2 != 0 일 경우 'B'이어야 한다. 만약 'B'가 아니라면 W를 1증가시킨다.
                    # 마찬가지로 8*8로 자른 체스판이 'B'로 시작할 경우 바꿔야 할 체스판의 개수는 B에 저장
                    if chess[i][j] != 'B':
                        W += 1
                    if chess[i][j] != 'W':
                        B += 1
        cnt.append(min(W,B))
print(min(cnt))