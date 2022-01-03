n = int(input())
a = []

for i in range(n):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    student = 0
    for score in a[1:]:
        if score > avg :
            student +=1
    rate = student / a[0] * 100
    print(f'{rate:.3f}%')