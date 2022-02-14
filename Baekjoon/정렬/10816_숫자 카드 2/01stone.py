# 10816 : 숫자 카드 2
'''
숫자 카드 : 정수 하나가 적혀져 있는 카드 
숫자 카드 N개를 갖고, 정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램 작성
'''
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_count = Counter(n_list)

for i in m_list:
    if i in n_count:
        print(n_count[i], end=' ')
    else:
        print(0, end=' ')

'''
# pypy3로 해도 시간초과 1

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_sort = sorted(list(set(n_list)))                               # 중복숫자 제거해서
n_count = [n_list.count(n_sort[i]) for i in range(len(n_sort))]  # 각 숫자의 갯수를 리스트로 만듦
                                                                 # 여기서 시간이 엄청 오래 걸릴 것을 알고 있긴 했음
n_dict = dict(zip(n_sort, n_count))                              # 각 숫자의 갯수를 알려주는 dict 생성

for i in m_list:
  if i in n_sort:
    print(n_dict.get(i), end=' ')
  else:
    print(0, end=' ')
'''

'''
# pypy3로 해도 시간초과 2

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_sort = sorted(n_list)
n_dict = {}
for i in n_list:
  if i in n_dict: n_dict[i] += 1
  else: n_dict[i] = 1

for i in m_list:
  if i in n_sort:
    print(n_dict.get(i), end=' ')
  else:
    print(0, end=' ')
'''