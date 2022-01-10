# 23253	: 자료구조는 정말 최고야 silver_4
'''
교과서 N권을 방 구석에 M개의 더미

N권의 교과서는 각각 1부터 N까지의 번호가 매겨져 있다. 
각 더미의 맨 위에 있는 교과서만 꺼낼 수 있으며, 반드시 꺼낸 순서대로 나열해야 하기 때문에 
번호순으로 나열하기 위해서는 1번, 2번, … N-1번, N번 교과서 순으로 꺼내야 한다.
'''
# dummy가 1이 아닌 경우 : 연속된 숫자 + 순차적 아니면 No
# 시간초과 pypy3로 통과했음..

n, m = map(int, input().split())
answer = True  # True면 yes 출력...

for _ in range(m):
    dummy = int(input())
    books = list(map(int, input().split()))

    for i in range(dummy-1): # dummy가 1일 경우 answer는 그냥 true 될듯?
        if books[i] == books[i]+1: # 연속된 숫자면 False
            answer = False
            break
        elif books[i] < books[i+1]: # 순차적 아니면 False
            answer = False
            break

print('Yes' if answer else 'No')
