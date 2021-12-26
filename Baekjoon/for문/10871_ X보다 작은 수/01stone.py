N, X = map(int, input().split())
sequence_list = list(map(int, input().split()))
for i in range(N):
    if sequence_list[i] < X:
        print(sequence_list[i], end=" ")