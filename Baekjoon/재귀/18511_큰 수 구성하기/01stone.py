# 18511 : 큰 수 구성하기
# 재귀 버림...ㅎ...product 함수로 구현하면 재귀겠지 뭐...
from itertools import permutations, combinations, product

n, k = map(int, input().split())
k_list = list(map(str, input().split()))
length = len(str(n))

while True:
    k_list_p = list(map(''.join, product(k_list, repeat = length)))
    answer = []
    for i in k_list_p:
        if int(i) <= n:
            answer.append(i)
    if len(answer) >= 1:
        print(max(answer))
        break
    else:
        length -= 1


'''
# 런타임 에러 : 100일 경우 2개만 뽑았을 때도 생각해야 해서 그런듯
k_list_p = list(map(''.join, product(k_list, repeat = len(str(n)))))

answer = []
for i in k_list_p:
  if int(i) <= n:
    answer.append(int(i))

print(max(answer))
'''