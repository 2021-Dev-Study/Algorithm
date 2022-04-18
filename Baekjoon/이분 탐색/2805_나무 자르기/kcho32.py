n, m = map(int, input().split())
tree_length = list(map(int, input().split()))
start, end = 1, max(tree_length)

while start <= end:
    mid = (start + end) // 2
    tmp_len = 0
    for length in tree_length:
        tmp_len += length - mid if length >= mid else 0   
    if tmp_len >= m: # 갯수가 많으면 길이가 짧은 것
        start = mid + 1
    else:
        end = mid - 1

print(end, start)
