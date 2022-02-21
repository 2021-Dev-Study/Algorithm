N, M = map(int, input().split())
 
d = min(N, M) # 더 작은 값을 기준으로 함 / 둘 중 최소길이가 사각형 최대라서...?
 
array = []
for _ in range(N):
    array.append(list(map(int, input())))
 
answer = 1 # 어떤 직사각형이 입력되든 가장 작은 정사각형 값은 1이므로 1로 초기화
for i in range(N):
    for j in range(M):
        for k in range(1, d):
            if i + k < N and j + k < M: # 인덱스 범위 안넘는 선에서 각 꼭짓점 비교 
                n = array[i][j]
                if n == array[i + k][j] and n == array[i][j + k] and n == array[i + k][j + k]:
                    answer = max(answer, (k + 1) ** 2) # 기존의 answer값과 새롭게 구한 넓이를 구해서 더 큰값을 answer에 대입 
 
print(answer)



