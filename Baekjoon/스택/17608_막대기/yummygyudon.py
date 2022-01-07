# 음.. 이게 왜 스택문제일까 궁금하네요..

import sys


# 어떻게 set로 해보려했는데 실패..
# stk = [None]*5
# n = int(sys.stdin.readline())
# stk = []
# cnt = 0
# ptr = 0
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     if ptr == 0:
#         stk[ptr] = num
#         continue
#     if num >= stk[ptr - 1]:
#         stk[ptr - 1] = num
#     else:
#         stk[ptr] = num
#
# print(set(stk)


## 런타임에러.... 멘붕
# n = int(sys.stdin.readline())
# cnt=0
# bar = []
#
# for _ in range(n):
#     bar.append(int(sys.stdin.readline()))
#
#
# stk =[]
# #내가 마주보는 사람에게 하나씩 순서대로 놔주는 모양새
# # stk에 들어있는 값은 상대방에게 보여주는 반대편에서 보는 가장 긴 막대의 값
# # (나) 5 4 3 2 1 (상대방) 이라면
# # 나에겐 5밖에 안보임(stk)
# # (나) 5 3 1 2 1 (상대방) 이라면
# # 처음에 1이 보였었지만 2막대가 더 크니 2가 보이기 때문에 1을 빼고 2를 넣어주고
# # 상대방에겐 현재 1보다 큰 2도 보일테니 cnt += 1
# for i in range(n-1, -1, -1): # 최근 들어갔던 막대부터 순서대로 하나씩 검사
#     if len(stk) == 0  : # 스택이 비어있으면
#         stk.append(bar[i]) # 가장 앞에 있던 막대
#         cnt += 1 # 1회
#     else :
#         if bar[i] > stk[-1] : # 가장 최근(top)이 막대보다 크면
#             stk.pop()
#             stk.append(bar[i])#내가 보는 가장 높은 막대
#             cnt+=1
#         # 기존 스택에 있던 막대보다 같거나 작은건 세지 않음.
#         # 어짜피 마주보는 상대방에게 안보여질 것이기 때문
# print(stk)

