import sys


n = int(sys.stdin.readline().rstrip())
str = []
nums = []
answer = 0

for i in range(n):
    str.append(int(sys.stdin.readline().rstrip()))

for num in str:
    if nums:
        if num == 0:
            nums.pop()
        else:
            nums.append(num)
    else:
        nums.append(num)

for num in nums:
    answer += num

print(answer)