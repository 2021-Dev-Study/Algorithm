import sys
n, m = map(int, sys.stdin.readline().split())
# 시간초과
# no_hear = []
# no_see =[]
# for i in range(1, n+m+1) :
#     name = sys.stdin.readline().rstrip()
#     if i >n :
#         no_see.append(name)
#     else :
#         no_hear.append(name)
# result =[]
# for p in no_see :
#     if p in no_hear :
#         result.append(p)
# result.sort()
# print(len(result))
# for i in result :
#     print(i)


no_hear = set()
no_see = set()
for _ in range(n) :
    no_hear.add(sys.stdin.readline().rstrip())
for _ in range(m) :
    no_see.add(sys.stdin.readline().rstrip())
result =sorted(list(no_hear & no_see))
print(len(result))
for name in result :
    print(name)
# 시간초과
# for i in range(1, n+m+1) :
#     name = sys.stdin.readline().rstrip()
#     if i >n :
#         no_see.add(name)
#     else :
#         no_hear.add(name)
# result =list(no_hear & no_see)
# print(len(result))
# for name in result[::-1] :
#     print(name)