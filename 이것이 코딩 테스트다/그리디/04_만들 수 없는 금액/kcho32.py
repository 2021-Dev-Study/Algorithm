n = int(input())
# money = sorted(list(map(int, input().split())), reverse=True)
coins = sorted(list(map(int, input().split())))
goal = 1
answer = 0

# while True:
#     if answer != 0:
#         break
    
#     tmp = goal
    
#     for i in money:
#         if i > tmp:
#             continue
#         else:
#             tmp -= i

#     if tmp:
#         answer = goal
#     else:
#         goal += 1

# print(goal)

## 시간 초과

for coin in coins:
    # 오름차 순 정렬 -> 작은 것부터
    # 타겟값을 만족하면 타겟값에 현재 동전값을 더한 것을 다음 타겟으로 정한다
    # 타겟값 + 동전값 - 1 만큼은 전부 표현 가능
    # 타겟 1, 동전 1로 만족 -> 다음 타겟은 2 -> 1까지 표현 가능
    # 타겟 2, 동전 2로 만족 -> 다음 타겟은 2+2 -> 3까지 표현 가능
    # 타겟 4, 3까지 표현 가능한 동전이 있기 때문에 4보다 작은 값의 동전만 있으면 표현 가능
    # 타겟 4 + coin, ...
    if coin > goal:
        break;
    else:
        goal += coin

print(goal)