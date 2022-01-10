import sys

n = int(input())
for i in range(n):
    ans = list(map(str, sys.stdin.readline().rstrip()))
    score = 0
    count = 0
    for j in ans:
        if j == "O":
            count += 1
            score += count

        elif j == "X":
            count = 0
    print(score)