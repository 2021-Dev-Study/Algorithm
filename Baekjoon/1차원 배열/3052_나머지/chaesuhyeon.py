a = []
b = []
for i in range(10):
    a.append(int(input()))
    b.append(a[i] % 42)
c = set(b)
print(len(c))