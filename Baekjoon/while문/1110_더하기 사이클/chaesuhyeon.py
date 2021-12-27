N = int(input())
count = 0
word = N
while True:
    a = word // 10
    b = word % 10
    c = (a+b) % 10
    word = (b*10) + c
    count +=1
    if word == N :
        break
print(count)
