import sys

T = int(sys.stdin.readline())
A = [0] * T
B = [0] * T

for i in range (0 ,T):
    A[i], B[i] = map(int, sys.stdin.readline().split())
    print(A[i]+B[i])

#for 안에서는 input()이 아니라 sys.stdin.readline()을 사용해야 함
