# 작성자: red-Pen9uin
# Data structure: word
# 10773: 제로
# 수행 결과: 31640 KB / 124 ms
"""
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다.
정수는 0에서 1,000,000 사이의 값을 가지며,
정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고,
아닐 경우 해당 수를 쓴다.

정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

"""
import sys


if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    index = -1
    stack = list()
    
    for _ in range(0, cnt):
        num = int(sys.stdin.readline())
        if num==0:
            del stack[index]
            index -= 1
        else:
            stack.append(num)
            index += 1
    
    print(f"{sum(stack)}")