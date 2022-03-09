n = int(input())
s_list = []

for k in range(n):
    w, h = map(int, input().split())
    s_list.append((w, h))

for i in s_list:
    rank = 1
    for j in s_list:
        if i[0] < j[0] and i[1] < j[1]:  # w, h 모두 본인보다 큰 사람
                rank += 1  # 덩치등수는 w, h 모두 큰 사람이므로
    print(rank, end = " ")