import sys
import re

ex = list(sys.stdin.readline().rstrip().split('-'))
start = 0
# 처음부터 끝까지 다 +일 때를 주의
for s in ex[0].split('+') :
    start += int(s)

for i in range(1, len(ex)) :
    s = 0
    nums = ex[i].split('+')
    for n in nums :
        s += int(n)
    start -= s
print(start)


# patter = re.complie('[0-9]')
# pattern = re.compile('[0-9]+')
# Corner = "55-50+40"
# a = pattern.findall(Corner)
# print(a)
# # nums =

# op = dict()
# op = []
# num = ""
# nums = []
# for s in ex :
#     if s == '+' or s == '-' :
#         nums.append(int(num))
#         num = ""
#         op.append(s)
#         # if s in op :
#         #     op[s] += 1
#         # else :
#         #     op[s] = 1
#     else :
#         num += s
# nums.append(int(num))
# nums.sort()
# op.sort(reverse = True)
