b = []
for i in range(9):
    b.append(int(input()))
max_b = max(b)
print(max_b)
print( b.index(max_b)+1)