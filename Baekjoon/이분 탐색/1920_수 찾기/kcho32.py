import sys

input = sys.stdin.readline

# def binary_search(array, target_num, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if array[mid] == target_num:
#         return 1
#     elif array[mid] < target_num:
#         # print(array[mid])
#         return binary_search(array, target_num, mid+1, end)
#     elif array[mid] > target_num:
#         # print(array[mid])
#         return binary_search(array, target_num, start, mid-1)

def binary_search(array, target_num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target_num:
            return 1
        elif array[mid] < target_num:
            start = mid+1
        elif array[mid] > target_num:
            end = mid-1
    return 0

n = int(input())
num_list = sorted(list(map(int, input().split())))
m = int(input())
target_nums = list(map(int, input().split()))

for target in target_nums:
    print(binary_search(num_list, target, 0, n - 1))