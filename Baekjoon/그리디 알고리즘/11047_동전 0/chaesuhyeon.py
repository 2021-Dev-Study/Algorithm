n, k = map(int, input().split())
arr = [None] * n

cnt = 0 

for i in range(n):
    arr[i] = int(input()) # 동전들 하나씩 입력받음


for i in range(n-1, -1, -1): # 큰 화폐 단위부터 체크 
    if arr[i] > k: # 만들어야하는 단위인 k보다 화폐단위가 큰 동전이라면 무시하고 다시 반복분 실행
        continue
    else: # k가 더 크다면
        cnt += k//arr[i] # k로 최대한 만들 수 있는 만큼 만들어야 하기 때문에 몫을 cnt에 더해줌  
        k %= arr[i] # k로 만들고 난 후의 나머지를 구함 
print(cnt) # 횟수 출력 