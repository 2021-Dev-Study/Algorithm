# 10815 : 숫자 카드
# 10816과 동일 

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
# 맞힌사람 코드
import sys

def test():
    
    input()
    b = set(input().split()) # 내가 가진 값
    input()
    d = input().split()      # 찾아야 하는 값
    
    res = ''
    for i in d:
        if i in b:
            res += '1 '
        else:
            res += '0 '
    
    print(res)

test()
'''