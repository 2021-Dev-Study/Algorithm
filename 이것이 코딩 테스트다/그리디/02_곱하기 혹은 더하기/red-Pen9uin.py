# 작성자: red-Pen9uin
# 1회차 작성
# 수행 결과:  KB /  ms

import sys
import time
start_time = time.time()

word = sys.stdin.readline().rstrip('\n')
num = 0

for i in word:
    
    if int(i)*num > 1:
        num *= int(i)
    else:
        num += int(i)

print(num)

end_time = time.time()
print(f"time : {end_time - start_time}")