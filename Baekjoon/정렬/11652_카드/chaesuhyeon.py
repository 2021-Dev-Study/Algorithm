import sys
from  collections import Counter

N = int(sys.stdin.readline().rstrip())
card = [0] * N

for i in range(N):
    card[i] = int(sys.stdin.readline())

card.sort()
counter = Counter(card).most_common()

# 정렬을 먼저 해주고 나면 무조건 (작은숫자 , 최대 개수) 가 먼저 나오기 때문에 [0][0]만 출력해준다.
print(counter[0][0])





