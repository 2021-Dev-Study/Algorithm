import sys
n = int(sys.stdin.readline())

# 너무 만만하게 봤네요
# for _ in range(n) :
#     s = sys.stdin.readline().rstrip()
#     left, right = 0, 0
#     for ps in s :
#         if ps =='(' :
#             left += 1
#         else :
#             right += 1
#     if left == right :
#         print('YES')
#     else :
#         print('NO')

for _ in range(n) :
    s = sys.stdin.readline().rstrip()
    left, right = 0, 0
    for ps in s :
        if ps =='(' :
            left += 1
        else :
            right += 1
            if left < right :
                break
    if left == right :
        print('YES')
    else :
        print('NO')
