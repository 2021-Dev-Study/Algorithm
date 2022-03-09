# 임의로 몇 개의 로프만 골라서 사용해도 되기 때문에
# 한개의 로프만 썼을 때부터 모든 로프를 사용했을 때 들 수 있는 경우의 수를 모두 생각해보고
# 그중 최댓값을 구하면 됨.
# 가장 작은 무게를 들수 있는 로프를 사용한다면 해당 무게를 로프의 갯수만큼 곱한 것이 그 로프를 사용했을 때 들 수 있는 최고 무게

# 로프의 무게순으로 정렬해서 큰 무게 가능 로프부터 "단독 사용 경우의 수"
# ~ 가장 작은 무게 가능 로프까지 " 자신보다 무거운 무게를 들 수 있는 모든 로프에게 자신의 최고무게를 적용시켜서 모든 로프를 같이 사용하는 경우의 수"

import sys
N = int(sys.stdin.readline())
rope = []
for _ in range(N) :
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True)
for i in range(N) :
    rope[i] = rope[i] * (i+1) # 최고무게 로프 단독사용 최고무게 ~ 최저무게 로프 모두 사용 최고무게
print(max(rope))