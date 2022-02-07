# 작성자: red-Pen9uin
# level 12: sort algorithm
# 1427_소트인사이드
# 수행 결과: 30864 KB / 68 ms
"""
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

"""

import sys


def solution(num):
    # solve = quick_sort(num, 0, len(num)-1)
    solve = merge_sort(num)
    return solve


def merge_sort(num):
    
    def _merge_sort(num, left: int, right: int) -> None:

        if left < right: # 조건을 만족할 경우에만 재귀 발생
            center = (left+right)//2

            _merge_sort(num, left, center)
            _merge_sort(num, center+1, right)

            p_index = p_buff = 0
            p_num = index = left

            while p_num <= center: # buff에 복사
                buff[p_index] = num[p_num]
                p_num += 1
                p_index += 1
            
            while p_num <= right and p_buff < p_index: # 병합
                if buff[p_buff] >= num[p_num]: # 내림차순
                    num[index] = buff[p_buff]
                    p_buff += 1
                else:
                    num[index] = num[p_num]
                    p_num += 1
                index += 1

            while p_buff < p_index: # 나머지 병합
                num[index] = buff[p_buff]
                p_buff += 1
                index += 1
        # end of _merge_sort

    buff = [None] * len(num)
    _merge_sort(num, 0, len(num)-1)
    del buff

    return num


if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    word = list()

    for _ in range(cnt):
        word.append(sys.stdin.readline().rstrip('\n'))

    word = solution(word)
    print(f"\n".join(word))