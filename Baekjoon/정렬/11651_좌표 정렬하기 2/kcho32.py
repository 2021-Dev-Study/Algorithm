import sys



n = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(n):
    nums.append(tuple(map(int, sys.stdin.readline().rstrip().split(" "))))
nums = sorted(nums, key=lambda x: (x[1], x[0])) 

for i in nums:
    sys.stdout.write(f'{" ".join(map(str, i))}\n')