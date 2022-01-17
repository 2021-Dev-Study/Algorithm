# 11116	: 교통량

from collections import deque

t = int(input())

for _ in range(t):

    m = int(input())
    left = deque(map(int, input().split()))
    right = deque(map(int, input().split()))
    count = 0

    while left:
        car = left.popleft()
        if car + 500 in left:  # t 일 때 1000인 바퀴와, t+500일 때 1500인 바퀴 둘 다 있으면 1이 count
            continue
        if car + 1000 in right: 
            count += 1

    print(count)








'''
left  : 235  451  735  951  2351 2851
right : 1235 1351 1451 1735 1851 1951

car = 235
    if 235 + 500 in left : True
    count = 0

car = 451
    if 451 + 500 in left : True
    count = 0

car = 735
    if 735 + 500 in left : False
    if 735 + 1000 in right : True
    count = 1

car = 951
    if 951 + 500 in left : False
    if 951 + 1000 in right : True
    count = 2

car = 2351
    if 2351 + 500 in left : True
    count = 2

car = 2851
    if 2851 + 500 in left : False
    if 2851 + 1000 in right : False
    count = 2
'''