d0 = [0] * 41
d1 = [0] * 41

def pibo(x, y):
    global cnt_1
    global cnt_0
    if x == 1:
        d1[y] += 1
        return 1
    if x == 0:
        d0[y] += 1
        return 0
    return pibo(x - 1, y) + pibo(x - 2, y)

n = int(input())
for i in range(n):
    x = int(input())
    pibo(x, x)
    print(d0[x], d1[x])