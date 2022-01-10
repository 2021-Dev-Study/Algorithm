import sys
    
n = int(input())
scores = list(map(int, sys.stdin.readline().split(" ")))
fake_s = 0

for i in range(len(scores)):
    fake_s += (scores[i] / max(scores) * 100)

print(fake_s / n)