import sys
from collections import Counter

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    note1 = Counter(map(int, sys.stdin.readline().rstrip().split(" ")))
    m = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    for i in note2:
        print("1" if note1[i] else "0")

