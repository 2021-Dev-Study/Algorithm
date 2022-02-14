# 3273 : 두 수의 합

# pypy3로 통과

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
x = int(input())
n_list.sort()

x_pair = []
for i in n_list:
  if x > i:
    if (x - i) in n_list:
      x_pair.append([i, x - i])
    else: pass
  else: pass

print(len(x_pair)//2)