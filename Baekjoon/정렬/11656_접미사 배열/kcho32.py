# import sys
# from itertools import islice

# str = sys.stdin.readline().rstrip()
# answer = []
# for i in range(len(str)):
#     answer.append("".join(list(islice(str, i, None))))

# print("\n".join(sorted(answer)))

import sys


str = sys.stdin.readline().rstrip()
answer = []
for i in range(len(str)):
    answer.append(str[i:])

print("\n".join(sorted(answer)))