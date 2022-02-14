import sys

n, *scores = sys.stdin.read().splitlines()
score_dict = dict({})

for i in scores:
    tmp = i.split(" ")
    score_dict[tmp[0]] = (int(tmp[1]), int(tmp[2]), int(tmp[3]))

answer = sorted(score_dict, key=lambda x: (-score_dict[x][0], score_dict[x][1], -score_dict[x][2], x))

print("\n".join(answer))