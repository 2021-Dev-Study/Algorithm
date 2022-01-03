N = int(input())
a = []
a = list(map(int, input().split()))
max_a = max(a)
score = []
for i in range(N):
    score.append(a[i]/max_a * 100)
print(sum(score)/N) 