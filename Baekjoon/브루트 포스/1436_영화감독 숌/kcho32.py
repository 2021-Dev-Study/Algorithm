cnt = 0
nums = 666
target = int(input())

while True:
    if '666' in str(nums):
        cnt += 1
        if cnt == target:
            print(nums)
            break
    nums += 1
