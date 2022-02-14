import sys
from collections import Counter


n = int(sys.stdin.readline().rstrip())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

# 입력 받은 수를 정렬 + nums_cnt에 각기 몇번 썼는지 저장 (Counter 사용)
nums = sorted(nums)
nums_cnt = Counter(nums)

avg = int(round(sum(nums)/len(nums), 0))
mid = nums[len(nums)//2]
# nums_cnt를 사용횟수를 기준으로 내림차 정렬 후, 첫번째와 두번째의 사용 갯수 같다면 두번째 저장. 
# 만약 숫자가 하나이거나 최다 사용한 숫자가 하나라면 첫번째 숫자 저장
most_list = sorted(nums_cnt, key = lambda x: nums_cnt[x], reverse = True)

if len(most_list) > 1:
    if nums_cnt[most_list[0]] == nums_cnt[most_list[1]]:
        most = most_list[1]
    else:
        most = most_list[0]
else:
    most = most_list[0]

range = nums[-1] - nums[0]

print(avg, mid, most, range, sep="\n")