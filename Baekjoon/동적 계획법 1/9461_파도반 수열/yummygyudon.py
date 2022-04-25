def pado(n) :
    if n >= 6 :
        for i in range(6, n+1) :
            basic.append(basic[i-1]+basic[i-5])

TC = int(input())
for _ in range(TC):
    N = int(input())
    basic = [0, 1, 1, 1, 2, 2]
    pado(N)
    print(basic[N])