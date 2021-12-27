N = int(input())
count = 0
n = N

while True:
    if 0 <= n < 10:
        n = n * 10 + n
    elif 10 <= n <= 99 :
        n = (n%10)*10 + (int(n/10) + n%10)%10
    count = count + 1

    if N == n:
        break

print(count)