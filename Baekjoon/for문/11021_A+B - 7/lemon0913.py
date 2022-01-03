import sys

T = int(sys.stdin.readline())
A = [0] * T
B = [0] * T

for i in range (0, T):
    A[i], B[i] = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {A[i]+B[i]}')