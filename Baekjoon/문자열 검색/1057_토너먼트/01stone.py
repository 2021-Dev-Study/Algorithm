# 1057 : 토너먼트

n, K, L = map(int, input().split())

'''
K_list = [K]
for i in range((K//2)-1):
  if K % 2 == 0:
    K_list.append(K_list[-1] // 2)
  else:
    K_list.append((K_list[-1] + 1) // 2)

L_list = [L]
for i in range((L//2)-1):
  if L % 2 == 0:
    L_list.append(L_list[-1] // 2)
  else:
    L_list.append((L_list[-1] + 1) // 2)

cnt = 0

while len(K_list) == 0:

# 굳이....? 이건 너무 번거로운데...?    
'''

cnt = 0

while K != L:
    K -= K // 2
    L -= L // 2
    cnt += 1

print(cnt)
