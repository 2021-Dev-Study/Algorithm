import sys


n = int(sys.stdin.readline().rstrip())

words = list(set(sys.stdin.readline().rstrip() for _ in range(n)))

words = sorted(words, key = lambda x: (len(x), x)) ## 처음에 len(x)로 비교하고 같으면 x 순으로 비교

sys.stdout.write("\n".join(words))