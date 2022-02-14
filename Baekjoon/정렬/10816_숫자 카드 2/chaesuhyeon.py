# 컴프리핸션 + join을 이용한 풀이
import sys
from  collections import Counter
N = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
counter = Counter(arr)

M = int(sys.stdin.readline())
num = sys.stdin.readline().split()

print(' '.join(f'{counter[m]}' if m in counter else '0' for m in num))


######## 두번째 풀이 ########
# 이분 탐색 ##  풀이 참고
import sys
N = int(sys.stdin.readline())
my_card = sorted([*map(int, input().split())])
M = int(sys.stdin.readline())
num_card =  [*map(int, input().split())]
answer = {}

# 개수 딕셔너리 생성
for i in my_card:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

# 이분 탐색 진행해서 target에 맞는 value값 return 받음
def binary(my_card, target, start, end):
    if start > end: # 존재하지 않으면 0 return
        return 0
    
    mid = (start + end) // 2

    if my_card[mid] == target:
        return answer.get(target) # value값 return 받음 

    elif target > my_card[mid] :
        return binary(my_card, target, mid+1, end)
    else:
        return binary(my_card, target, start, mid-1)

for target in num_card:
    print(binary(my_card, target, 0, len(my_card)-1), end=' ')



######## 맨 처음 풀이 시간 초과 ########
import sys
from  collections import Counter
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
# print("arr : ", arr)

counter = Counter(arr)

M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))


for i in range(M):
    if num[i] in arr:
        print(counter[num[i]], end= ' ')
    else:
        print(0, end=' ')
