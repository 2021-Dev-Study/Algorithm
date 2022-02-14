# 작성자: red-Pen9uin
# Classification: sort algorithm
# 1764_듣보잡
# 수행 결과: 52368 KB / 344 ms
"""
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.

이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며,
그 길이는 20 이하이다.
N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며,
보도 못한 사람의 명단도 마찬가지이다.


듣보잡의 수와 그 명단을 사전순으로 출력한다.
"""

import sys
from unittest import result

# def solution(not_heard, not_heard_list, not_seen, not_seen_list):
#     not_heard_nor_seen = list()
    
#     not_heard_list.sort()
#     not_seen_list.sort()

#     if not_heard > not_seen:
#         find_list = not_seen_list
#         from_list = not_heard_list
#     else:
#         find_list = not_heard_list
#         from_list = not_seen_list

#     for this_name in find_list:
#         is_found = binary_search(this_name, from_list, 0, len(find_list)-1)

#         if is_found:
#             not_heard_nor_seen.append(is_found)
#             # print(not_heard_nor_seen)
#         else:
#             pass

#     return not_heard_nor_seen


# def binary_search(target, from_list, left, right):
#     middle_idx = (left+right)//2
#     # print(middle_idx)
#     middle = from_list[middle_idx]

#     if left > right:
#         return False

#     if target == middle:
#         # print('answer {}'.format(middle_idx))
#         return target
#     elif middle > target:
#         result = binary_search(target, from_list, left, middle_idx-1)
#     elif middle < target:
#         result = binary_search(target, from_list, middle_idx+1, right)
#     else: 
#         return False
    
#     return result


if __name__ == "__main__":
    not_heard, not_seen = map(int, sys.stdin.readline().split())
    not_heard_list = [None] * not_heard
    not_seen_list = [None] * not_seen

    for i in range(not_heard):
        not_heard_list[i] = sys.stdin.readline().rstrip('\n')
    for i in range(not_seen):
        not_seen_list[i] = sys.stdin.readline().rstrip('\n')

    # result = solution(not_heard, not_heard_list, not_seen, not_seen_list)

    not_heard_list = set(not_heard_list)
    not_seen_list = set(not_seen_list)
    result = list(not_heard_list & not_seen_list)
    result.sort()

    print(f"{len(result)}")
    print("\n".join(i for i in result))