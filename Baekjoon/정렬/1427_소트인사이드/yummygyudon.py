# 문자열로서 나누면 모두 한자릿수 숫자이기 때문에
# Counting Sort로 해결
def Counting_Sort(ary) :
    n = len(ary)
    freq = [0] * 10
    tmp = [0] * n
    for i in range(n) :
        freq[ary[i]] += 1
    for i in range(1, 10) :
        freq[i] += freq[i-1]
    for i in range(n-1, -1, -1) :
        freq[ary[i]] -= 1
        tmp[freq[ary[i]]] = ary[i]
    for i in range(n) :
        ary[i] = tmp[i]

import sys
NUM = sys.stdin.readline().rstrip()
ary = []
for i in NUM :
    ary.append(int(i))
Counting_Sort(ary)
for _ in range(len(ary)) :
    print(ary.pop(),end='')

# 메모리 : 30864KB / 시간 : 69ms