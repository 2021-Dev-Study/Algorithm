# 1302 : 베스트셀러
# 11652 유사


import sys
input = sys.stdin.readline

n = int(input())
n_dic = {}

for i in range(n):
    title = str(input())
    if title in n_dic:
        n_dic[title] += 1
    else:
        n_dic[title] = 1

n_dic = sorted(n_dic.items(), key=lambda x: (-x[1], x[0]))
print(n_dic[0][0])