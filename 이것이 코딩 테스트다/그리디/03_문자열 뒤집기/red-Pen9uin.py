# 작성자: red-Pen9uin
# 1회차 작성
# 수행 결과:  KB /  ms

import sys
# import time
# start_time = time.time()

num = sys.stdin.readline().rstrip('\n')
turn_over = 0
flag = False

for i in range(len(num)-1):
    if num[i] != num[i+1]:
        if flag:
            turn_over += 1
            flag = False
        else:
            flag = True

if flag:
            turn_over += 1
            flag = False

print(turn_over)

# end_time = time.time()
# print(f"time : {end_time - start_time}")