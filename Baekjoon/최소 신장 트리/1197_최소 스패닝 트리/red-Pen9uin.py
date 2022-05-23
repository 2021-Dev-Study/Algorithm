# 작성자: red-Pen9uin
# 작성일: 2022-5-23
# Classification: 최소 스패닝 트리

import sys

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    points = [i for i in range(V+1)]
    lines = []

    for _ in range(E):
        lines.append(list(map(int, sys.stdin.readline().split())))

    lines.sort(key=lambda x: x[2])

    def find(x):
        if x != points[x]:
            points[x] = find(points[x])
        return points[x]

    answer = 0
    for start, end, weight in lines:
        s_point = find(start)
        e_point = find(end)

        if s_point != e_point:
            if s_point < e_point:
                points[s_point] = e_point
            else: # s_point >= e_point
                points[e_point] = s_point

            answer += weight
    
    print(answer)