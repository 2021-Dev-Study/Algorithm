s = input()
cnt_0 = 0
cnt_1 = 0

if s[0] == '0':
  cnt_0 += 1
else:
  cnt_1 += 1

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    if s[i+1] == '1':
      cnt_0 += 1
    else:
      cnt_1 += 1
  
print(min(cnt_0, cnt_1))