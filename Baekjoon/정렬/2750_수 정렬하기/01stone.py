# 2750 : 수 정렬하기
# 삽입정렬

'''
n = int(input())
n_list = [int(input()) for i in range(n)]
n_list.sort()
for i in n_list:
    print(i)
'''

n = int(input())
n_list = [int(input()) for _ in range(n)]


for i in range(1, len(n_list)):
    while i > 0 and n_list[i-1] > n_list[i]:
        n_list[i-1], n_list[i] = n_list[i], n_list[i-1]
        i -= 1
    
for j in n_list:
    print(j)
