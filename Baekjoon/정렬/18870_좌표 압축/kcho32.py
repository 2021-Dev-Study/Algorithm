from collections import Counter
import sys

# 정렬
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# nums_cnt = Counter(nums)
# nums_cnt_sorted = sorted(nums_cnt)

nums_setted = list(set(nums))
nums_sorted = sorted(nums_setted)
# 카운트를 진행했지만 결구 필요없었음... 그냥 세트로 해도 됨

answer = {}

for i in range(len(nums_sorted)):
    answer[nums_sorted[i]] = i


for j in nums:
    print(answer[j], end = " ")

