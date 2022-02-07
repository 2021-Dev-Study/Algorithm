import sys

n = int(sys.stdin.readline().rstrip())
nums: list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# 셸 정렬
# h = n // 2

# while h > 0:
#     for i in range(h, n):
#         j = i - h
#         tmp = nums[i]

#         while j >= 0 and nums[j] > tmp:
#             nums[j+h] = nums[j]
#             j -= h
        
#         nums[j+h] = tmp
    
#     h //= 2

# print("\n".join(list(map(str, nums))))


sorted_nums: list = sorted(nums)

print("\n".join(list(map(str, nums))))