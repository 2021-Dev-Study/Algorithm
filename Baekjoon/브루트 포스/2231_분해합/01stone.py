n = int(input())
result = 0
for i in range(1, n+1):  # 1부터 n까지
    div_n_list = list(map(int, str(i)))  # 각 자리수 리스트
    sum_n = i + sum(div_n_list)  # 분해합
    if sum_n == n:  # 분해합 = n
        result = i  # 네놈이다..
        break
print(result)