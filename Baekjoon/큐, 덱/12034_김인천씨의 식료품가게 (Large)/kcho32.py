import sys
from collections import deque

# case = int(sys.stdin.readline().rstrip())

# for i in range(case):
#     grocery = int(sys.stdin.readline().rstrip())
#     price = deque(sys.stdin.readline().rstrip().split())
#     temp = []

#     for j in range(len(price)):
#         if price:
#             x = int(price.popleft())
#             count = 0
#             while price:
#                 count += 1

#                 if int(x // 0.75) == int(price[0]) and x * 4 % 3 == 0:
#                     temp.append(int(x))
#                     price.popleft()
#                     break
#                 else:
#                     price.rotate(-1)
            
#                 if count == len(price):
#                     price.append(int(x))
#                     break
    
#     answer = f'Case #{i+1}: '
#     for i in sorted(temp):
#         answer += f' {str(i)}'
#     print(answer)


case = int(sys.stdin.readline().rstrip())

for i in range(case):
    grocery = int(sys.stdin.readline().rstrip())
    price = deque(sys.stdin.readline().rstrip().split())
    temp = []
    
    ## temp 리스트에 물품 개수만큼의 세일한 가격이 들어갈 때 까지 반복
    while len(temp) != grocery:
        # 가장 저렴이부터 시작해서
        x = price.popleft()
        # 할인 가격이 price에 포함되면
        # temp에 올리고 price에서 제거
        if str(int(int(x) // 0.75)) in price:
            temp.append(x)
            price.remove(str(int(int(x) // 0.75)))
            
    print(f'Case #{i+1}: {" ".join(temp)}')