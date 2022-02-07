# 작성자: red-Pen9uin
# level 12: sort algorithm
# 11651_좌표 정렬하기 2
# 수행 결과: 50856 KB / 1076 ms
"""
만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면,
모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.

수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다.
이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은
Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한
결과 X'1, X'2, ..., X'N를 출력해보자.

"""

import sys
import copy

def solution(cnt, num):
    arr = [0] * cnt
    # min_num = min(num)

    # for i in range(cnt):
    #     if num[i] == min_num:
    #         arr[i] = 0
    #     elif num[i] == max_num:
    #         arr[i] = 



if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    locate = list(map(int, sys.stdin.readline().split()))

    locate_set = solution(cnt, locate)
    
    print(locate)
    print(locate_set)

    for l in locate:
        print(f"{locate_set.index(l)}", end=' ')