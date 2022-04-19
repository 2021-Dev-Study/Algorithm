# 내 풀이
S = input()

alpha = []
result = 0

for s in S:
    if s.isdigit():
        result += int(s)
    else:
        alpha.append(s)

alpha.sort()

for i in alpha:
    print(i, end='')
print(result)

# 책 풀이
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))        