# 9 9 12 12 12 15 16 20
# d :  9
# data :  deque([9, 12, 12, 12, 15, 16, 20])
# discount :  7
# price :  [9]
# data after append(d) :  deque([9, 12, 12, 12, 15, 16, 20, 9])
# d :  9
# data :  deque([12, 12, 12, 15, 16, 20, 9])
# discount :  7
# price :  [9, 9]
# data after append(d) :  deque([12, 12, 12, 15, 16, 20, 9, 9])
# d :  12
# data :  deque([12, 12, 15, 16, 20, 9, 9])
# discount :  9
# data after remove discount :  deque([12, 12, 15, 16, 20, 9])
# d :  12
# data :  deque([12, 15, 16, 20, 9])
# discount :  9
# data after remove discount :  deque([12, 15, 16, 20])
# d :  12
# data :  deque([15, 16, 20])
# discount :  9
# price :  [9, 9, 12]
# data after append(d) :  deque([15, 16, 20, 12])
# d :  15
# data :  deque([16, 20, 12])
# discount :  11
# price :  [9, 9, 12, 15]
# data after append(d) :  deque([16, 20, 12, 15])
# Case #1: 9 9 12 15

import sys
from collections import deque
T = int(input())

for i in range(1,T+1):
    N = int(input()) # 상품수
    price = [] # 할인 가격만 담을 곳 
    data = deque(map(int, sys.stdin.readline().rstrip().split())) # 정렬된 값들을 입력받음

    while len(price) < N: # 할인된 가격이 상품 수만큼 찼을 때 반복문 종료 
        if data:
            d = data.popleft() # 맨 앞 숫자 뽑음

            discount = round(d * 0.75) # 그 숫자에서 75%할인된 가격을 discount로 저장 

            if discount in data: # discount된 가격이 data에 있다면
                data.remove(discount) # data에서 그 가격을 삭제 

            else: # discount 가격이 data에 없다면 d는 이미 어떤 물건의 할인된 가격이므로 price에 저장 후 data에도 저장 
                price.append(d)
                data.append(d) # data에도 저장해야지 if discount in data 를 판단하여 price에 안넣을 수 있음 

    print(f'Case #{i}: ', end = '') # 출력 형식
    for j in range(len(price)-1):
        print(price[j], end=' ') 
    print(price[-1])

############################################################# 중복값 체크 x
# import sys
# from collections import deque
# T = int(input())
# price = []
# for i in range(1,T+1):
#     N = int(input())
#     data = deque(map(int, sys.stdin.readline().rstrip().split()))

#     while len(data) > N:
#         if data:
#             d = data.popleft()
#             print("d : ", d)
#             discount = round(d * 0.75)
#             print("discount : ", discount)
#             print("data : ", data)
#             if discount in data:
#                 print("data2 : ", data)
#                 continue
#             else:
#                 price.append(d)
#                 data.append(d)
#                 print("price : ", price)

#     print(f'Case #{i}: ', end = '')
#     for j in price:
#         print(j, end=' ')

    # print(f'Case #{i}: ', end = '')
    # for j in range(len(data)-1):
    #     print(data[j], end=' ')
    # print(data[-1])