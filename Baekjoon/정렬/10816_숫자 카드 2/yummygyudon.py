import sys
# 시간 초과
# N = int(sys.stdin.readline())
# card = list(sys.stdin.readline().rstrip().split())
# M = int(sys.stdin.readline())
# numbers = list(sys.stdin.readline().rstrip().split())
# # d = dict.fromkeys(numbers, 0) # set를 dict의 키로 적용
# # for k in d.keys():
# #     d[k] = card.count(k)

# 런타임 에러
# N = int(sys.stdin.readline())
# card = list(sys.stdin.readline().rstrip().split())
# M = int(sys.stdin.readline())
# numbers = list(sys.stdin.readline().rstrip().split())
# d = {num : card.count(num) for num in numbers }
# for num in numbers :
#     print(d[num], end=' ')


## PyPy3로 하니까 통과 _ 852ms
N = int(sys.stdin.readline())
card = list(sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline())
numbers = list(sys.stdin.readline().rstrip().split())
d = {}
for c in card : # 우선 card에 있는 유효값들 먼저 dict로 만들어주기
    # numbers의 수가 card에 없으면 그냥 0 출력하면 됨
    if c in d :
        d[c] += 1
    else :
        d[c] = 1
print(' '.join(str(d[num]) if num in d else '0' for num in numbers))
