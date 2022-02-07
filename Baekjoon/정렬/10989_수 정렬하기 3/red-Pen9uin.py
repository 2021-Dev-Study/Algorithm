# 작성자: red-Pen9uin
# level 12: sort algorithm
# 10989_수 정렬하기 3
# 수행 결과: 30864 KB / 9764 ms
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

메모리 제한: 8MB
아예 num 배열에 저장하면 안된다..!
"""

import sys
  

if __name__ == "__main__":
    num_cnt = int(sys.stdin.readline())
    cnt = [0] * (10000 + 1) # for range 1 ~ 10000
    
    for _ in range(num_cnt):
        num = int(sys.stdin.readline())
        cnt[num] += 1

    for i in range(0, len(cnt)):
        if cnt[i]!=0:
            for _ in range(cnt[i]):
                print(f"{i}")