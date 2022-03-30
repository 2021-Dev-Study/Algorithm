def match(arr, key, rot, r, c):
    n = len(key)

    # 열쇠 복사
    for i in range(n):
        for j in range(n):
            if rot == 0: # 회전 값이 0이면 그대로니까 그냥 복사
                arr[r+i][c+j] += key[i][j] # 대입이 아닌 더해줘야 각 칸의 합을 알 수 있음
            elif rot == 1: # 시계방향으로 90도 회전
                arr[r+i][c+j] += key[n-1-j][i]
            elif rot == 2:
                arr[r+i][c+j] += key[n-1-i][n-1-j]
            else:
                arr[r+i][c+j] += key[j][n-1-i]

def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True # for문이 다 끝날 때까지 False를 return 안했다는 말은 모두 1이라는 뜻. True반환



def solution(key,lock):
    offset = len(key)-1 # 자물쇠와 떨어진 거리

    # 자물쇠 가운데 복사
    for r in range(offset+ len(lock)): # 행 / 자물쇠랑 떨어진 거리 + 자물쇠 길이 만큼까지 가야함
        for c in range(offset + len(lock)): # 열 / 자물쇠랑 떨어진 거리 + 자물쇠 길이 만큼까지 가야함
            
            # 4방향으로 회전
            for rot in range(4):
                arr = [[0 for _ in range(58)] for _ in range(58)]

                # 자물쇠 복사
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset+i][offset+j] = lock[i][j] # offset만큼 떨어진 곳에 자물쇠 복사

                match(arr, key, rot, r, c )
                if check(arr, offset, len(lock)):
                    return True # 모두 1이라면 바로 True return        
    return False # 모든 경우에 대해서 True가 아니라면 여기까지 와서 False반환
