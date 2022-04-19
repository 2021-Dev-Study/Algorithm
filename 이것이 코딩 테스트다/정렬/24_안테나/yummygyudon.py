N = int(input())
house = list(map(int, input().split()))
# 심심풀이 땅콩
# mn = 1e9
# result = -1
# for i in range(N) :
#     s = 0
#     h = house[i]
#     for k in range(N):
#         s += abs(h-house[k])
#     if s < mn :
#         mn = s
#         result = i
# print(house[result])
house.sort()
print(house[(N-1)//2])
# if N % 2 == 0 :
#     print(house[(N//2)-1]) # 중간 - 1 : index때문에
# else :
#     print(house[(N+1 // 2) - 1])