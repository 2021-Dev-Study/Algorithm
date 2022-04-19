import sys

n = list(sys.stdin.readline().rstrip())
first = sum(map(int, n[:len(n)//2]))
second = sum(map(int, n[len(n)//2:]))

print("LUCKY") if first == second else print("READY")