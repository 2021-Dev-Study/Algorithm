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


n = int(input())
nums = list(enumerate(map(int, input().split())))
answer = [-1 for i in range(n)]
stack = []

for idx, num in nums:
    if stack:
        x = nums[stack[-1]][1]
        comp = num
        if x >= num:
            stack.append(idx)
        else:
            while stack:
                y = stack.pop()
                
                if nums[y][1] < comp:
                    comp = nums[y][1]
                
                answer[y] = comp
    else:
        stack.append(idx)
print(answer)
"""




"""