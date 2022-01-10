n = 10
result = 1
storage = []
num_count = []

for i in range(3):
    result *= int(input())

remain_num = result

while True:
    if remain_num // 10 > 0:
        storage.append(remain_num % 10)
        remain_num //= 10
    elif remain_num // 10 == 0:
        storage.append(remain_num)
        break

for i in range(n):
    count = 0
    for j in range(len(storage)):
        if i == storage[j]:
            count += 1

    num_count.append(count)
    print(num_count[i])