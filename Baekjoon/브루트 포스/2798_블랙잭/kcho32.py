# ## itertools를 사용한 경우

# from itertools import combinations, filterfalse

# n, target = map(int, input().split(" "))
# card_list = list(map(int, input().split(" ")))

# ## 겹치지 않는 모든 3 콤비네이션 중 target보다 작거나 같은 것만 필터링
# answer_list = list(filter(lambda x: sum(x) <= target, combinations(card_list, 3)))

# #정렬 후 가장 합이 가장 큰 수를 출력
# print(sum(sorted(answer_list, key=lambda x: sum(x))[-1]))
# # print(sum(answer_list[-1]))

## itertools를 사용하지 않은 경우

n, target = map(int, input().split(" "))
card_list = list(map(int, input().split(" ")))

max_sum = 0
first, second, third = 0, 1, 2

for i in range(first, len(card_list)-2):
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            if (card_list[i] + card_list[j] + card_list[k]) <= target and (card_list[i] + card_list[j] + card_list[k]) > max_sum:
                max_sum = card_list[i] + card_list[j] + card_list[k]

print(max_sum)
