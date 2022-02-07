# 작성자: red-Pen9uin
# level 12: sort algorithm
# 2750_수 정렬하기
# 수행 결과: 30864 KB / 176 ms
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

"""
import sys


def solution(num):
    solve = shaker_sort(num)
    return solve


# def bubble_sort(num):
#     # Simple Bubble sort
#     length = len(num)
#     arr = num

#     for i in range(0, length-1):
#         for j in range(length-1, i, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
    
#     return arr


def shaker_sort(num):
    left = 0
    right = len(num)-1
    arr = num
    
    while left < right:
        for i in range(right, left, -1):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                last = i
        left = last

        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last = i
        right = last

    return arr
                


if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    num = list()
    for _ in range(cnt):
        num.append(int(sys.stdin.readline()))

    num = solution(num)
    print(f"\n".join(str(i) for i in num))