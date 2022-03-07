# 작성자: red-Pen9uin
# level 11: brute force
# 7568_덩치
# 수행 결과: 30864 KB / 68 ms
"""
첫 줄에는 전체 사람의 수 N이 주어진다.
그리고 이어지는 N개의 줄에는
각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

여러분은 입력에 나열된 사람의 덩치 등수를 구해서
그 순서대로 첫 줄에 출력해야 한다.

단, 각 덩치 등수는 공백문자로 분리되어야 한다.
"""

import sys

if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    people = [None]*cnt
    for i in range(cnt):
        people[i] = list(map(int, sys.stdin.readline().split()))
    ranking = [0]*cnt

    for i in range(cnt):
        rank = 1
        for j in range(cnt):
            if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
                rank += 1
        ranking[i] = rank

    print(" ".join(str(i) for i in ranking))
