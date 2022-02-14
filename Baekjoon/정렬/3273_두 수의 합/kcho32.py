import sys

from itertools import combinations, dropwhile

n, data, x = map(str, sys.stdin.read().splitlines())
count = 0

## itertools의 combination을 통해 모든 조합을 만들고 비교 -> 메모리 너무 커서 실패

# data = data.split(" ")
# data = list(dropwhile(lambda a: int(a) > int(x), data))

# for i in list(combinations(data, 2)):
#     if int(i[0]) + int(i[1]) == int(x):
#         count += 1

# print(count)

## 정렬 후 작은 수 큰수 조합으로 비교후 범위 
data = list(map(int, data.split(" ")))
data = list(dropwhile(lambda a: a > int(x), data))
data.sort()
front = 0
back = len(data) - 1

while front < back:
    if data[front] + data[back] == int(x):
        count += 1
        front += 1
    elif data[front] + data[back] > int(x):
        back -= 1
    else:
        front += 1
print(count)


"""
1 2 3 4 5 6 7 8의 조합 중 0를 찾는다면
1, 8 -> 9 : count++
2, 9 = 11 > 9
2, 8 = 10 > 9 
2, 7 = 9 == 9 -> count++
...
"""