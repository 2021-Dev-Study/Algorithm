n = 10
n_list = []
for i in range(n):
    n_list.append(int(input()) % 42)
n_list = list(set(n_list))

print(len(n_list))