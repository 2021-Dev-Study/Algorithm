from collections import deque
N, M = map(int, input().split())
nums = list(range(N))
leaf_board = [M-1]*N
q = deque()
q.append([0,1])
tree = []
while q :
    parent, child = q.popleft()
    if child >= N :
        continue
    if parent == 0 :
        tree.append([parent, child])
        q.append([child, child+1])
        continue
    if leaf_board[parent] > 0 :
        tree.append([parent, child])
        q.append([parent, child+1])
        leaf_board[parent] -= 1
    else :
        # tree.append([child, child+1])
        q.append([child-1, child-1+1])
for t in tree :
    print(f"{t[0]} {t[1]}")

# N, M =map(int, input().split())
# # N = 5 , M = 3
#
# print("0 1")
# last_leaf = 1
# leaf = 0
# for i in range(2, N) :
#     if M-1> leaf : # m-1 == 2
#         print(f"{last_leaf} {i}") # 1 2, 1 3
#         leaf +=1
#     else :
#         last_leaf = i-1 # 3
#         print(f"{last_leaf} {i}")