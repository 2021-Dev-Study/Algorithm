from itertools import permutations

nums: list = [i for i in range(1, int(input()) + 1)]

for i in list(permutations(nums, len(nums), )):
    print(" ".join(map(str, i)))
