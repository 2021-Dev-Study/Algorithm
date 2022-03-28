N, combi = map(int, input().split())
# balls = set(map(int, input().split()))
# balls = sorted(list(balls))
# from itertools import combinations
# c = combinations(balls, 2)
# print(list(c))

balls = list(map(int, input().split()))
balls.sort()
result = 0
for i in range(len(balls)) :
    a = balls[i]
    for k in range(i+1 , len(balls)) :
        b = balls[k]
        if a != b :
            result+=1
print(result)
