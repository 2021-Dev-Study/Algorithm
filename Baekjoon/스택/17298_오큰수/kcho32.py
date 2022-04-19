# n = int(input())
# nums = list(map(int, input().split()))
# answer = []

# for i in range(n - 1):
#     tmp = -1
#     for j in range(i + 1, n):
#         if nums[i] < nums[j]:
#             tmp = nums[j]
#             break
#     answer.append(tmp)
# answer.append(-1)  

# print(" ".join(list(map(str, answer))))

from collections import deque

n = int(input())
nums = deque(list(enumerate(map(int, input().split()))))
answer = [-1 for i in range(n)]
stack = []
x = nums.pop()

while True:
    if not nums:
        break
    if not stack:
        stack.append(nums.pop())
    else:
        if nums[-1][1] <= stack[-1][1]:
            stack.append(nums.pop())
            print(nums)
            print(stack)
        else:
            while stack:
                idx, num = stack.pop()
                answer[idx] = x[1]
            x = nums.pop()

print(answer)