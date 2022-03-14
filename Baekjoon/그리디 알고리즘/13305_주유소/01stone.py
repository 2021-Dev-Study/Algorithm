n = int(input())
road_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))

min_oil = city_list[0]
answer = 0

for i in range(n-1):
  if min_oil > city_list[i]:
    min_oil = city_list[i]
  answer += (min_oil * road_list[i])

print(answer)