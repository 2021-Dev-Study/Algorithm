# n: 동전의 종류
# target_price: 해당 동전을 통해 만들고 싶은 값
n, target_price = map(int, input().split())

# n개의 종류의 동전을 리스트에 넣어준다. -> 이미 오름차 정렬이고 스택을 사용할 것이기 때문에 deque 미사용
coins = [int(input()) for i in range(n)]
count = 0 # 사용된 동전 갯수

# 큰 동전부터 사용하면 최소한의 동전을 사용 갯수를 알 수 있다
while True:
    if target_price == 0: # 루프 초반엔 break 조건을 둔다. 
        break

    coin = coins.pop() # 가장 큰 동전부터
    
    if coin > target_price: # 동전 종류가 원하는 값보다 클 경우, 사용 불가이므로 넘어간다.
        continue
    else:
        count += target_price // coin # ex) 4200원에서는 일단 1000원짜리 4개가 필요 -> 4200 // 1000의 몫 
        target_price %= coin # ex) 4200에서 1000으로 나눈 후 나머지 값이 200원이 남음.

print(count)