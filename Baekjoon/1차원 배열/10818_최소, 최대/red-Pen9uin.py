# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 10818: 최소, 최대
"""
N개의 정수가 주어진다.
이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

"""
import sys

def main():
    num = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    # min = 1000000 # Max value
    # max = -1000000 # Min value
    min = arr[0] # First value
    max = arr[0] # First value
    for i in range(0,num):
        min = min if min<arr[i] else arr[i]
        max = max if max>arr[i] else arr[i]
    print(f"{min} {max}")

if __name__ == "__main__":
    main()