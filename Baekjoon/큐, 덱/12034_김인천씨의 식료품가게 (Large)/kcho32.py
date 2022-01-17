import sys
from collections import deque

case = int(sys.stdin.readline().rstrip())



for i in range(case):
    grocery = int(sys.stdin.readline().rstrip())
    price = deque(sys.stdin.readline().rstrip().split())
    temp = []

    # for j in range(len(price)):
    #     if price:
    #         x = int(price.popleft())
    #         count = 0
    #         while price:
    #             count += 1

    #             if int(x // 0.75) == int(price[0]) and x * 4 % 3 == 0:
    #                 temp.append(int(x))
    #                 price.popleft()
    #                 break
    #             else:
    #                 price.rotate(-1)
            
    #             if count == len(price):
    #                 price.append(int(x))
    #                 break
    
    # answer = f'Case #{i+1}: '
    # for i in sorted(temp):
    #     answer += f' {str(i)}'
    # print(answer)

    while len(temp) != grocery:
        x = price.popleft()
        
        if str(int(int(x) // 0.75)) in price:
            temp.append(x)
            price.remove(str(int(int(x) // 0.75)))
        
    print(f'Case #{i+1}: {" ".join(temp)}')