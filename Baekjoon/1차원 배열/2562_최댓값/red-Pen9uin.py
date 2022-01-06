# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 2562: 최댓값
"""
9개의 서로 다른 자연수가 주어질 때,
이들 중 최댓값을 찾고
그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

"""
import sys

def main():
    MAX_ARR_NUM = 9
    arr = list()
    for i in range(0,MAX_ARR_NUM):
        arr.append(int(sys.stdin.readline()))

    max = 0 # Min value

    for i in range(0,MAX_ARR_NUM):
        if max<arr[i]:
            max = arr[i]
            index = i
    print(f"{max}\n{index+1}")

if __name__ == "__main__":
    main()