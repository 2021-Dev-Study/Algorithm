eq = input().split('-')
answer = []
for i in eq:
  # print('i', i)
  cnt = 0
  f = i.split('+')
  for j in f:
    # print(j)
    cnt += int(j)
  answer.append(cnt)
# print(answer)

num = answer[0]
for i in range(1, len(answer)):
  # print(answer[i])
  num -= answer[i]
print(num)