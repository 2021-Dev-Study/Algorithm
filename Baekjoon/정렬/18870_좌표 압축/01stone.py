# 18870	: 좌표 압축
# 기억이 안난다...시간초과로 애먹었던거 말고는...
# 답 베껴왔나????


n = int(input())
n_list = list(map(int, input().split()))

n_sort = sorted(list(set(n_list)))

n_dic = {n_sort[i]:i for i in range(len(n_sort))} 
for i in n_list: 
  print(n_dic[i],end=' ')