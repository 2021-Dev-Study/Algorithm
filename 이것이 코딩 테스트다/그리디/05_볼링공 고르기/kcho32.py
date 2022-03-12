n, m = map(int, input().split())
balls = list(map(int, input().split()))
answer = 0

for i in range(len(balls) - 1):
    ball = balls.pop()
    for second_ball in balls:
        if ball == second_ball:
            continue
        else:
            answer += 1

print(answer)
