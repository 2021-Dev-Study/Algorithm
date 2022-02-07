# 1427 : 소트인사이드


'''
n = input()
n = [int(i) for i in n]

n_sort = sorted(n, reverse=True)

for j in n_sort:
    print(j, end='')
'''

n = input()
n = [int(i) for i in n]

for i in range(1, len(n)):
    while i > 0 and n[i-1] > n[i]:
        n[i-1], n[i] = n[i], n[i-1]
        i -= 1

for j in n[::-1]:
    print(j, end='')