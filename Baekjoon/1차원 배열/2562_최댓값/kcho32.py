n: int = 9
storage = []
for i in range(n):
    storage.append(int(input()))
print(max(storage))
print(storage.index(max(storage))+1)