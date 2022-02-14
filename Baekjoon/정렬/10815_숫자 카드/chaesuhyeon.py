import sys
N = int(sys.stdin.readline())
arr = set(map(int,sys.stdin.readline().split())) # 순서와 중복에 대한 특성을 사용하지 않을때는 list보다는 set을 사용하는게 좋음
M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
for i in range(M):
    if num[i] in arr :
        print(1 , end=" ")
    else:
        print(0, end = " ")

# 이분탐색으로 풀이 공부..
import sys
N = int(sys.stdin.readline())
my_card = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_card = list(map(int, sys.stdin.readline().split()))
answer = []

def binary(k, my_card, start, end):
    mid = (start + end ) // 2
    if start > end:
        answer.append(str(0))
    elif k == my_card[mid]:
        answer.append(str(1))
    elif k > my_card[mid]:
        binary(k, my_card, mid+1, end)
    else:
        binary(k, my_card, start, mid-1)

for k in num_card:
    start = 0
    end = len(my_card)-1
    binary(k, my_card, start, end)

print(' '.join(answer))

# 시간 초과 #
import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split())) ## 이 부분 때문에 시간 초과 
M = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
for i in range(M):
    if num[i] in arr :
        print(1 , end=" ")
    else:
        print(0, end = " ")


