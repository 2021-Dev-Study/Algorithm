n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])

for i in range(n):
    grade = 1 # 기본 1로 설정 
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: # 다음값과 비교해서 다음값이 두개 다 큰 경우 +1해줌
            grade = grade + 1
    print(grade,end=" ")  # 이어서 출력