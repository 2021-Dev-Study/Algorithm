# 작성자: red-Pen9uin
# level 12: sort algorithm
# 2751_수 정렬하기 2
# 수행 결과: 149808 KB / 6980 ms
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

"""
# 시간복잡도 O(nlogn)을 가지는정렬을 사용해야 통과가 가능한 문제

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
                if buff[p_buff] <= num[p_num]: # 오름차순
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
    num = list()
    for _ in range(cnt):
        num.append(int(sys.stdin.readline()))

    num = solution(num)
    print(f"\n".join(str(i) for i in num))


# def simple_insert_sort(num):
#     # simple_insert_sort
#     length = len(num)

#     for i in range(0, length):
#         tmp = num[i]
#         j = i
#         while j>0 and num[j-1]>tmp:
#             num[j] = num[j-1]
#             j -= 1
#         num[j] = tmp
    
#     return num


# def quick_sort(num, left, right):
#     index_stack = list()
#     index_stack.append((left, right))

#     if len(num) < 9:
#         result = simple_insert_sort(num)
#         return result
    
#     # # 처음-가운데-끝 중 중간값 구하기
#     # if num[left] > num[right] : num[left],num[right] = num[right],num[left]
#     # if num[left] > num[pivot] : num[left],num[pivot] = num[pivot],num[left]
#     # if num[pivot] > num[right] : num[right],num[pivot] = num[pivot],num[right]
    
#     # num[right-1],num[pivot] = num[pivot],num[right-1]
#     # left += 1
#     # right -= 2
    
#     while len(index_stack) > 0:
#         pl, pr = left, right = index_stack.pop()
#         # pivot = (left+right)//2
#         # num_pivot = num[pivot]
#         num_pivot = num[(pl+pr)//2]

#         while pl <= pr:
#             while num[pl] < num_pivot: pl += 1 # breaks when num[left] >= num_pivot
#             while num[pr] > num_pivot: pr -= 1 # breaks when num[right] <= num_pivot
#             # now : num_pivot <= num[left] && num[right] <= num_pivot
            
#             if pl <= pr:
#                 # swap num[left] and num[right]
#                 # bigger number goes to right side of list
#                 num[pl],num[pr] = num[pr],num[pl]
#                 # and go on...
#                 pl += 1
#                 pr -= 1
#         # ends when left >= right

#         # index status:     [i_left         right  left          i_right]
#         if left < pr: index_stack.append((left, pr))
#             # False:  when [right i_left           left          i_right]
#         if pl < right: index_stack.append((pl, right))
#             # False:  when [i_left         right            i_right left]

#     # both False:     when [right i_left                    i_right left]
#     # == sort complete.

#     return num