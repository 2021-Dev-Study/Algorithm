# 작성자: red-Pen9uin
# 작성일: 2022-5-23
# Classification: 최소 스패닝 트리

"""
N개의 정점이 있을 때
최소 N-1개의 간선으로 연결이 될 수 있고
그렇다면 트리의 구조가된다.

신장 트리는 모든 정점이 연결되어 있어야하고
사이클을 포함하지 않는다.

즉 이 문제에서는 국가의 수 -1이 답이된다.
"""

import sys

if __name__ == "__main__" :
    cases = int(sys.stdin.readline())

    for i in range(cases):
        n, m = map(int, sys.stdin.readline().split())
        for j in range(m):
            a, b = map(int, sys.stdin.readline().split())
        print(n - 1)