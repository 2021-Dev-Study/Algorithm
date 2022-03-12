n, k = map(int, input().split())
cnt = 0

while n > 1:
    if n % k:
        n -= 1
        cnt += 1
    else:
        if n // k < n - 1:
            n //= k
            cnt += 1
        else:
            n -= 1
            cnt += 1

print(cnt)