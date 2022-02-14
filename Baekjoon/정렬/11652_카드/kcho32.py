from collections import Counter
import sys

n, *nums = map(int, sys.stdin.readlines())
nums_cnt = Counter(nums)
nums = dict(nums_cnt)
nums = sorted(nums, key=lambda x: (nums_cnt[x], -x), reverse = True)
print(nums[0])

