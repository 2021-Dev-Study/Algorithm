import sys


n, m = map(int, sys.stdin.readline().rstrip().split(" "))
not_heard = set({})
not_seen = set({})

for _ in range(n):
    not_heard.add(sys.stdin.readline().rstrip())

for _ in range(m):
    not_seen.add(sys.stdin.readline().rstrip())

not_heard_and_seen = list(not_heard & not_seen)
not_heard_and_seen.sort()

print(len(not_heard_and_seen))
print("\n".join(not_heard_and_seen))


