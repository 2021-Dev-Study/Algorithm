# 작성자: red-Pen9uin
# Data structure: stack
# 17608: 막대기
"""
첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000)이 주어지고
이어지는 N줄 각각에는
막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다.

오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수를 출력한다.

"""
import sys

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    stick = list()
    for _ in range(0, num):
        stick.append(int(sys.stdin.readline()))
    
    shown = stick[num-1]
    count = 1

    for i in reversed(range(0, num)):
        if stick[i] > shown:
            count += 1
            shown = stick[i]
    
    print(count)