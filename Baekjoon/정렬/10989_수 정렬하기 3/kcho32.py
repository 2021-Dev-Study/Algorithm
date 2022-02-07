# import sys
# from collections import Counter

# n = int(sys.stdin.readline().rstrip())
# nums: list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# num_cnt = Counter(nums)
# num_cnt_max = max(num_cnt)
# counting_array = [None] * (num_cnt_max + 1)
# answer = [None] * n

# for i in range(num_cnt_max + 1):
#     if not i:
#         counting_array[i] = num_cnt[i]
#     else:
#         counting_array[i] = num_cnt[i] + counting_array[i-1]

# for j in nums:
#     answer[counting_array[j]-1] = j
#     counting_array[j] -= 1

# print("\n".join(list(map(str, answer))))

##해당 방식으로 풀 경우, 메모리 초과가 뜬다 -> 모든 수를 다 저장하므로
# import sys
# from collections import Counter

# n = int(sys.stdin.readline().rstrip())
# num_cnt = Counter({})

# for i in range(n):
#     num_cnt[int(sys.stdin.readline().rstrip())] += 1

# num_cnt_max = max(num_cnt)
# counting_array = [0] * (num_cnt_max + 1)
# answer = [0] * n

# for i in range(num_cnt_max + 1):
#     if not i:
#         counting_array[i] = num_cnt[i]
#     else:
#         counting_array[i] = num_cnt[i] + counting_array[i-1]

# for j in num_cnt:
#     for _ in range(num_cnt[j]):
#         answer[counting_array[j]-1] = str(j)
#         counting_array[j] -= 1

# sys.stdout.write("\n".join(answer))
# for k in answer:
#     print(k)

############################### try 3 ###############################################
import sys
from collections import Counter


# 값을 입력 받아서 리스트로 저장하면 메모리 초과 -> 저장하지 않고 카운트만 하기
n = int(sys.stdin.readline().rstrip())
num_cnt = Counter({})

for i in range(n):
    num_cnt[int(sys.stdin.readline().rstrip())] += 1

# 10001개의 공간 (0 ~ 10000)을 만들어 각 숫자가 몇번 쓰였는지를 num_cnt를 통해 넣어준다
num_cnt_max = max(num_cnt)
counting_array = [0] * 10001

for i in range(10001):
    counting_array[i] = num_cnt[i]
# index j 의 값이 해당 값과 같고, value값은 몇번 쓰였는지 저장되어 있다. -> value값 만큼 반복해서 j값 반복
for j in range(len(counting_array)):
    for k in range(counting_array[j]):
        print(j)
        
