# 처음풀이 17점.. 너무 단순하게 생각함,, (이전 지역의 가격만 고려) --> 최소 가격이 나오면 그 가격으로 주유해서 쭉 가는게 나은데.., 고려 안했음

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = distance[0] * price[0] # 첫 시작 

for i in range(1, len(distance)): # 두번째 원소부터 비교
    if price[i-1] >= price[i]: # 전 지역의 가격이 더 클경우
        result += (price[i] * distance[i]) # 그냥 위아래 곱함
    else: # 전 지역의 가격이 저렴할 경우
        result += (price[i-1] * distance[i]) # 현재 거리 수 * 전 지역의 주유소 가격

print(result)


# 다른 풀이
n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
min_price = price[0] # 첫번째 값으로 초기화 (무조건 처음 가격으로 주유를 해야하므로)
for i in range(n-1):
    if price[i] < min_price: # 가격이 더 작은 주유소가 나오면 그 주유소 가격으로 바꿔줌
        min_price = price[i]
    result += (min_price * distance[i])
print(result)