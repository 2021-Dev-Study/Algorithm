# 예제는 통과하는데 틀린 코드

import sys
n = int(sys.stdin.readline().rstrip())
arr = [] # 데이터 입력 받기 위한 리스트
result = [] # 계산을 위한 리스트
num = [] # 결과값 담을 리스트

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort() # 카드 묶음 순서대로 정렬

i = 0

while True:
    print("i :", i)
    if i == n: # i가 카드 묶음 개수가 되면 반복문 종료
        num.append(sum(result))  # 종료 전에 result에 담긴 데이터의 합을 num에 추가하고 종료
        break

    if len(result) == 2: # result에 담긴 묶음의 개수가 두개라면
        print("result 두번째 : ", result)

        num.append(sum(result)) # 그때까지의 묶음 합을 num 리스트에 추가
        print("num : ", num)
        result = [] # result를 다시 비워줌
        result.append(num[-1]) # 비운 리스트에 다시 num에 마지막에 추가된(직전의 결과값) 합을 result에 추가해서 계산 다시 수행
        print("result num값 추가 : ", result)

    else: # result에 담긴 묶음의 개수가 2개가 아니라면
        result.append(arr[i]) # result 리스트에 카드 묶음을 추가해주고
        i += 1 # i 증가
        print("result 첫번째 : ", result)    

print(sum(num)) #  num에 담긴 데이터(묶음들의 합)의 합을 구함

# 30 40 50 100
# 30 40 = 70
# 70 + 50 = 120
# 120 + 100 = 220 

# 30 40 50 60
# 30 40 = 70
# 70 50 = 120
# 120 60 = 180

#  책 풀이
import heapq
n = int(input())

heap=[]
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) != 1 :
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap,sum_value)
print(result)