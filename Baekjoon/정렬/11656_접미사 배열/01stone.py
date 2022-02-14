# 11656 : 접미사 배열

s = str(input())
s_suffix = []
for i in range(len(s)):
  s_suffix.append(s[i:])

s_suffix.sort()
for j in s_suffix:
  print(j)