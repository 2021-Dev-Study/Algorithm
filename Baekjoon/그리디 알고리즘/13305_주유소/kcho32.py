import sys
# city_num: 도시 수
# roads_length: 도로의 길이
# oil_cost: 각 도시별 오일 가격
# min_oil_cost: 현재 마을에서까지의 제일 쌌던 기름 가격
# total_charge: 최종적으로 기름에 사용한 돈
city_num = int(sys.stdin.readline())
roads_length = list(map(int, sys.stdin.readline().split()))
oil_cost = list(map(int, sys.stdin.readline().split()))
min_oil_cost = oil_cost[0] # 처음 시작을 시작점의 오일 가격으로 놓고 일단은 산다..
total_charge = 0

# 시작 마을에서는 무조건 기름을 사야되기 때문에 min_oil_cost를 시작가격으로 초기화하고
# 다음 마을에서는 min_oil_cost와 비교해서 싼 걸로 기름을 산다.
# 다음 마을에서 비교하고 저번 마을에서 산다는게 말은 안되지만 된다고 치자
# 당장 싼걸로 사기 때문에 그리디 알고리즘 사용 가능.
for i in range(len(oil_cost) - 1):
    if oil_cost[i] >= min_oil_cost:
        total_charge += min_oil_cost * roads_length[i]
    else:
        min_oil_cost = oil_cost[i]
        total_charge += min_oil_cost * roads_length[i]

print(total_charge)