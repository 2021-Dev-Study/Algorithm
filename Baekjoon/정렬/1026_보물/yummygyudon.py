# A의 가장 큰수 & B의 가장 작은 수를 곱하고
# B의 가장 큰수 & A의 가장 작은 수를 곱하면 가장 작은 값 구할 수 있음.

import sys
n = int(sys.stdin.readline())
arrA = list(map(int, sys.stdin.readline().rstrip().split()))
arrB = list(map(int, sys.stdin.readline().rstrip().split()))
arrA.sort() ; arrB.sort(reverse=True)

# print(arrA)
# print(arrB)
sum = 0
for i in range(n):
    sum += arrA[i]*arrB[i]

print(sum)