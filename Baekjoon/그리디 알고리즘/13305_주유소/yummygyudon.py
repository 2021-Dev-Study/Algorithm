N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
total = 0
cost = price[0]
for i in range(N-1) :
    if cost > price[i] :
        cost = price[i]
    total += cost*distance[i]
print(total)