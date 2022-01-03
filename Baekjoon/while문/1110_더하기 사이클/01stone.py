n_input = int(input())
n = n_input
cnt = 0

while True:
    n_sum = (n//10) + (n%10)
    n_new = ((n%10)*10) + (n_sum%10)
    cnt += 1
    if n_new == n_input:
        break
    n = n_new
print(cnt)