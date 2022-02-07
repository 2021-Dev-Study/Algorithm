# 작성자: red-Pen9uin
# level 12: sort algorithm
# 2108_통계학
# 수행 결과: 53172 KB / 3240 ms
"""
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
단, N은 홀수이다.
그 다음 N개의 줄에는 정수들이 주어진다.
입력되는 정수의 절댓값은 4,000을 넘지 않는다.

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

"""

import sys


def solution(num):
    center = len(num)//2
    num = merge_sort(num)

    # print("=====================")
    print(f"{round(sum(num)/len(num))}") # 평균
    print(f"{num[center]}") # 중앙값
    
    most = get_the_most(num)
    print(f"{most}") # 최빈값
    
    print(f"{max(num) - min(num)}") # 범위


def get_the_most(num):
    most = []
    best = 0
    count = 0
    now = num[0]

    for n in num:
        if n == now:
            count += 1
        else:
            count = 1
            now = n
        
        if count == best:
            most.append(n)
        elif count > best:
            most = [n]
            best = count
    
    # most = set(most)
    if len(most)>1:
        result = most[1]
    else:
        result = most[0]
    return result


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

    solution(num)