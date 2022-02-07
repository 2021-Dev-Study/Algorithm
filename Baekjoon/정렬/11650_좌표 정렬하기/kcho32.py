import sys

n = int(sys.stdin.readline().rstrip())
nums: list = []

for _ in range(n):
    nums.append(tuple(map(int, sys.stdin.readline().rstrip().split(" "))))

nums = sorted(nums)

for i in nums:
    sys.stdout.write(f'{" ".join(map(str, i))}\n')