# 5568 : 카드 놓기

from itertools import permutations  # 코테에서 이용 가능

n = int(input())
k = int(input())
n_list = [input().rstrip() for _ in range(n)]

answer = set()
for i in permutations(n_list, k):
    # print(i, end='')            # ('1', '2')('1', '12')('1', '1')('2', '1')('2', '12')('2', '1')('12', '1')('12', '2')('12', '1')('1', '1')('1', '2')('1', '12')
    # print(''.join(i), end=', ') # 12, 112, 11, 21, 212, 21, 121, 122, 121, 11, 12, 112,
    answer.add(''.join(i))

# print(answer)  # {'21', '11', '122', '112', '121', '12', '212'}
print(len(answer))





'''
# dfs로 순열 구현 : 찾아봄
def permutations(n_list, x):
    result = []
    previous_elements = []
    
    def dfs(elements):
        if len(elements) == (len(n_list)-x):
            result.append(previous_elements[:]) # previous_elements를 append로 넣으면 previous_elements가 변경되었을 때 append로 넣은 값이 바뀌게 되므로
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            previous_elements.append(e)
            dfs(next_elements)
            previous_elements.pop()
    dfs(n_list)
    return result
'''