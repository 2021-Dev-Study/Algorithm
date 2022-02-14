import sys

# 정렬
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# nums_cnt = Counter(nums)
# nums_cnt_sorted = sorted(nums_cnt)
# 카운트를 진행했지만 결구 필요없었음... 그냥 세트로 해도 됨 -> 중복 삭제 후 진행
# 정렬 진행 후 인덱스 -> 정답

nums_setted = list(set(nums))
nums_sorted = sorted(nums_setted)

answer = {}

for i in range(len(nums_sorted)):
    answer[nums_sorted[i]] = i


for j in nums:
    print(answer[j], end = " ")