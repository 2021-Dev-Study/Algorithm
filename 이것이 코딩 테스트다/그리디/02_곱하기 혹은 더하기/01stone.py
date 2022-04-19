
s = list(map(str, input()))
# print(s)

answer = int(s[0])
for i in range(1, len(s)):
  num = int(s[i])
  if (num <= 1) or (answer <= 1):
    answer += num
  else:
    answer *= num

print(answer)
