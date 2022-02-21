n = int(input())
six = 666
cnt = 0
while True:
    if '666' in str(six):
        cnt += 1
    if cnt == n:
        print(six)
        break
    six += 1