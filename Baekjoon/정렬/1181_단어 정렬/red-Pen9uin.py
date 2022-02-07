# 작성자: red-Pen9uin
# level 12: sort algorithm
# 1181_단어 정렬
# 수행 결과: 35472 KB / 240 ms
"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

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
                if len(buff[p_buff]) < len(num[p_num]): # 오름차순
                    num[index] = buff[p_buff]
                    p_buff += 1

                elif len(buff[p_buff]) == len(num[p_num]): # 길이가 같다
                    if buff[p_buff] <= num[p_num]: # 오름차순
                        num[index] = buff[p_buff]
                        p_buff += 1
                    else:
                        num[index] = num[p_num]
                        p_num += 1
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
    
    word = list(set(word))
    word = solution(word)
    # print(word)
    print(f"\n".join(word))