# 2108 : 통계학


from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
 
# 산술평균 : 다 더해서 / n
print(round(sum(n_list)/n))
 
# 중앙값 : 오름차순 -> 중간값
n_list.sort()
print(n_list[n//2])
 
# 최빈값 : 빈출
cnt_li = Counter(n_list).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
# 범위 : 최댓값-최솟값
print(max(n_list)-min(n_list))