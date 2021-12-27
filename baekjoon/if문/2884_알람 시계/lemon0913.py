H, M = map(int, input().split())

if (H == 0) and (M < 45):
    H = 23
    M = M + 15

else:
    time = H*60 + M - 45
    H = int(time / 60)
    M = time % 60


print(H, M)

