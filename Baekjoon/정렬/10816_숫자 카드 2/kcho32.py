from typing import MutableSequence, Sequence
import sys
from collections import Counter


# def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
#     pa, pb, pc = 0, 0, 0  # 각 배열의 커서
#     na, nb, nc = len(a), len(b), len(c)

#     while pa < na and pb < nb:
#         if a[pa] <= b[pb]:
#             c[pc] = a[pa]
#             pa += 1
#         else:
#             c[pc] = b[pb]
#             pb += 1
#         pc += 1
#     ## 다 하고나서 마지막으로 남은 pa나 pb는 아래서 더해준다
#     while pa < na:
#         c[pc] = a[pa]
#         pa += 1
#         pc += 1
    
#     while pb < na:
#         c[pc] = b[pb]
#         pb += 1
#         pc += 1

# def merge_sort(a: MutableSequence) -> None:
#     def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
#         if left < right:
#             center = (left + right) // 2

#             _merge_sort(a, left, center)
#             _merge_sort(a, center + 1, right)

#             p = j = 0
#             i = k = left

#             while i <= center:
#                 buff[p] = a[i]
#                 p += 1
#                 i += 1

#             while i <= right and j < p:
#                 if buff[j] <= a[i]:
#                     a[k] = buff[j]
#                     j += 1
#                 else:
#                     a[k] = a[i]
#                     i += 1
#                 k += 1

#             while j < p:
#                 a[k] = buff[j]
#                 k += 1
#                 j += 1            
    
#     n = len(a)
#     buff = [None] * n
#     _merge_sort(a, 0, n - 1)
#     del buff

n = int(sys.stdin.readline().rstrip())
nums = Counter({})

for i in list(map(int, sys.stdin.readline().rstrip().split(" "))):
    nums[i] += 1

m = int(sys.stdin.readline().rstrip())
for j in list(map(int, sys.stdin.readline().rstrip().split(" "))):
    if nums[j]:
        print("1", end=" ")
    else:
        print("0", end=" ")

