import sys
from collections import Counter


# 값을 입력 받아서 리스트로 저장하면 메모리 초과 -> 저장하지 않고 카운트만 하기
n = int(sys.stdin.readline().rstrip())
num_cnt = Counter({})
sorted_list = []
answer = 0
tmp = 0

for i in list(map(int, sys.stdin.readline().rstrip().split(" "))):
    num_cnt[i] += 1

# 1001개의 공간 (0 ~ 1000)을 만들어 각 숫자가 몇번 쓰였는지를 num_cnt를 통해 넣어준다
counting_array = [0] * 1001

for i in range(1001):
    counting_array[i] = num_cnt[i]
# index j 의 값이 해당 값과 같고, value값은 몇번 쓰였는지 저장되어 있다. -> value값 만큼 반복해서 j값 반복
for j in range(len(counting_array)):
    for k in range(counting_array[j]):
        tmp += j
        answer += tmp

print(answer)

