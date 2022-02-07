# 작성자: red-Pen9uin
# level 12: sort algorithm
# 11651_좌표 정렬하기 2
# 수행 결과: 50856 KB / 1076 ms
"""
2차원 평면 위의 점 N개가 주어진다.

좌표를 y좌표가 증가하는 순으로,
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음
출력하는 프로그램을 작성하시오.

"""

import sys


def solution(num):
    # solve = quick_sort(num, 0, len(num)-1)
    # print("==============")
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
                if buff[p_buff][1] < num[p_num][1]: # 오름차순 x좌표
                    num[index] = buff[p_buff]
                    p_buff += 1

                elif buff[p_buff][1] == num[p_num][1]: # 길이가 같다
                    if buff[p_buff][0] < num[p_num][0]: # 오름차순 y좌표
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
    locate = list()

    for _ in range(cnt):
        locate.append(list(map(int, sys.stdin.readline().split())))

    locate = solution(locate)
    # print(locate)
    for l in locate:
        print(f"{l[0]} {l[1]}")