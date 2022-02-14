# 2217 : 로프
'''
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 
각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
>> 최대 중량 : w/k * k
로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
'''

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

max_w = []
for i in range(len(rope)):
    # print(i+1, rope[i])
    max_w.append((i+1) * rope[i])

print(max(max_w))



'''
# 맞힌 사람 코드

import sys
In = sys.stdin.readline

def main():

    n = int(In())
    rope = [0] * 10001
    
    for _ in range(n):
        rope[int(In())] += 1
    
    m, s = 0, 0
    for x in range(10000,-1,-1):
        s += rope[x]
        m = max(m, x * s)
    
    print(m)
main()
'''