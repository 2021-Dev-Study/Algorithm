def merge_sort(ary) :
    def _merge_sort(ary, l, r) :
        if l < r :
            center = (l+r) //2

            _merge_sort(ary, l, center)
            _merge_sort(ary, center+1, r)

            p = j = 0
            i = k = l

            while i <= center :
                tmp[p] = ary[i]
                p += 1
                i += 1
            while i <= r and j < p :
                if tmp[j] <= ary[i] :
                    ary[k] = tmp[j]
                    j += 1
                else :
                    ary[k] = ary[i]
                    i += 1
                k += 1
            while j < p :
                ary[k] = tmp[j]
                k += 1
                j += 1
    n = len(ary)
    tmp = [None] * n
    _merge_sort(ary, 0, (n-1))

import sys
N = int(sys.stdin.readline())
ary = []
for _ in range(N):
    ary.append(int(sys.stdin.readline()))
merge_sort(ary)
# 산술평균
print(round(sum(ary)/N))

# 중앙값 _ N은 홀수인점 주의
print(ary[(N-1)//2])

# 최빈값
# # dictionary로 해결 : 런타임 에러가 나네요...
# keys = list(set(ary))
# values = [0] * len(keys)
# d = {str(x) : y for x, y in zip(keys, values)}
# # print(d)
# for k in ary :
#     d[str(k)] += 1
# m_value = max(d.values())
# m_key = []
# for item in d.items():
#     if item[1] == m_value :
#         m_key.append(item[0])
# # merge sort를 했을 때 작은 수들이 가장 앞(왼쪽)에 있기 때문에
# # item에서 최빈값 ket만 append를 하더라도 작은 순서대로 들어가서
# # 여러개일 경우 두번째로 작은수 : index가 1인 값
# print(m_key[1])

# collections - Counter 해결
from collections import Counter
Count = Counter(ary).most_common()
if len(Count) >= 2 :
    if Count[0][1] == Count[1][1] :
        print(Count[1][0])
    else :
        print(Count[0][0])
else:
    print(Count[0][0])

# 범위
print(ary[-1] -ary[0])

# 메모리 : 55784KB / 시간 : 3040ms