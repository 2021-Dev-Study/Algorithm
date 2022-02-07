import sys
N = int(sys.stdin.readline())
ls = set()
num = list(map(int,sys.stdin.readline().rstrip().split()))
ls = sorted(list(set(num)))
d = {ls[i] : i for i in range(len(ls))}
# ls = list(map(str,ls))
for n in num :
   print(d[n], end=' ')

# for n in num :
#     ls.add(n)

# ls = list(set(num))
# def Counting_Sort(ary) :
#     n = len(ary)
#     freq = [0] * 10
#     tmp = [0] * n
#     for i in range(n) :
#         freq[ary[i]] += 1
#     for i in range(1, 10) :
#         freq[i] += freq[i-1]
#     for i in range(n-1, -1, -1) :
#         freq[ary[i]] -= 1
#         tmp[freq[ary[i]]] = ary[i]
#     for i in range(n) :
#         ary[i] = tmp[i]

# for n in num :
#     cnt = 0
#     while True:
#         for i in ls :
#             if n == i :
#                 break
#             else :
#                 cnt += 1
#                 continue
#         break
#     print(cnt, end=' ')



# 와 도저히 시간초과 문제 해결을 못해서 검색해보니 dictionary를 사용하는군요
# 메모리 : 148208KB / 시간 : 2124ms