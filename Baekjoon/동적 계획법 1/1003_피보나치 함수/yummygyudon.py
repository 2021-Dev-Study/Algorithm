import sys
input = sys.stdin.readline
TC = int(input())

def fibo(n) :
    fibo_basic = [[1, 0], [0, 1], [1, 1]]
    if n >= 3 :
        for i in range(3, n+1):
            fibo_basic.append([ fibo_basic[i-1][0]+fibo_basic[i-2][0],
                                fibo_basic[i-1][1]+fibo_basic[i-2][1]])
    print(f"{fibo_basic[n][0]} {fibo_basic[n][1]}")

for i in range(TC) :
    N = int(input())
    fibo(N)