import sys
from collections import Counter


n = int(sys.stdin.readline().rstrip())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

nums = sorted(nums)
nums_cnt = Counter(nums)

avg = int(round(sum(nums)/len(nums), 0))
mid = nums[len(nums)//2]
most_list = sorted(nums_cnt, key = lambda x: nums_cnt[x], reverse = True)

if len(most_list) > 1:
    if nums_cnt[most_list[0]] == nums_cnt[most_list[1]]:
        most = most_list[1]
    else:
        most = most_list[0]
else:
    most = most_list[0]

range = nums[-1] - nums[0]

print(avg, mid, most, range, sep="\n")