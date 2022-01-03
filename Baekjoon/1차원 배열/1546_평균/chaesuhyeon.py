N = int(input())
a = []
a = list(map(int, input().split()))
max_a = max(a)
score = []
for i in range(N): # 과목의 개수만큼 반복
    score.append(a[i]/max_a * 100) # 새로운 점수를 구함
print(sum(score)/N)  # 점수를 과목의 개수로 나눔