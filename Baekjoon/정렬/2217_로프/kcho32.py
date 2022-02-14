from collections import deque
import sys

# n = int(input())
# nums = [int(input()) for i in range(n)]
# max_num = 0

# nums = deque(sorted(nums))
# while nums:
#     tmp = nums.popleft() * n
#     n -= 1

#     if tmp > max_num:
#         max_num = tmp
    
# print(max_num)
################################################################################
# n = int(input())
# nums = [int(input()) for i in range(n)]
# nums.sort()

# print(max(nums[i] * (n - i) for i in range(n)))

################################################################################
# n = int(input())
# nums = [int(input()) for i in range(n)]
# nums.sort()

# print(max(nums[i] * (n - i) for i in range(n-1, -1, -1)))

################################################################################

n, *data=map(int,sys.stdin.readlines()) ## 왜 빠름?
data.sort()
print(max(data[-i]*(i) for i in range(1,n+1)))
