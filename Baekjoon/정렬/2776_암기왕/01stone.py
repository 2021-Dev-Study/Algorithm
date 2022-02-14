# 2776 : 암기왕
'''
# 틀렸습니다~!~!~!

t = int(input())
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)
'''
# pypy3로 통과

import sys
input = sys.stdin.readline

# t = int(input())
for _ in range(int(input())):
    n = int(input())
    n_list = set(map(int, input().split()))  # 중복 제거 : 있으면 그냥 1 적으면 되니까~!
    m = int(input())
    m_list = list(map(int, input().split()))

    for i in m_list:
        if i in n_list: print(1)
        else: print(0)
        # print(1 if i in n_list else 0)