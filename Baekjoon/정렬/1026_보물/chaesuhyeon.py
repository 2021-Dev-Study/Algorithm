# 0 1 1 1 6
# 8 7 3 2 1
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()

m = 0
sum = 0
i = 0
while i < len(A):
    m = max(B) # B에서 최댓값을 뽑고
    p = B.pop(B.index(m)) # 최댓값의 인덱스를 구해서 그 인덱스의 값을 pop해서 최댓값 뽑음
    sum += A[i] * p # 그 최댓값과 A의 최솟값을 곱함
    i += 1 # 인덱스 늘려가며 A의 최솟값과 B의 최댓값을 곱해줌
print(sum) # 합계 출력 
