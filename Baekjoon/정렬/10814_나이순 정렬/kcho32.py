# 만약 나이가 같을 경우, 들어온 순서로 비교
# enumerate로 인덱스를 붙여 먼저 들어온 순 = index로 함
# sorted => 퀵 + 병합 (+ 귀찮)이라서 사용
# import sys
# import enum

# n = int(sys.stdin.readline().rstrip())
# info = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]
# info = list(x for x in enumerate(info))
# info = sorted(info, key = lambda x: (int(x[1][0]), x[0]))
# for i in info:
#     print(i[1][0], i[1][1])

import sys

n = int(sys.stdin.readline().rstrip())
info = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]
info = sorted(info, key = lambda x: (int(x[0])))
print(info)