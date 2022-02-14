from collections import Counter
n = int(input())
book = [0] * n
for i in range(n):
    book[i] = input()

book.sort()
count = Counter(book).most_common()
print(count[0][0])