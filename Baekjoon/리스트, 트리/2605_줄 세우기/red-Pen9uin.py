# 작성자: red-Pen9uin
# Classification: list, tree
# 2605_줄 세우기
# 수행 결과:  KB /  ms
"""
https://www.acmicpc.net/problem/2605

첫째 줄에는 학생의 수가 주어지고 둘째 줄에는 줄을 선 차례대로 학생들이 뽑은 번호가 주어진다. 학생의 수가 100 이하이고,
학생들이 뽑는 번호는 0 또는 자연수이며 학생들이 뽑은 번호 사이에는 빈 칸이 하나씩 있다.

학생들이 처음에 줄을 선 순서대로 1번부터 번호를 매길 때, 첫째 줄에 학생들이 최종적으로 줄을 선 순서를 그 번호로 출력한다. 학생 번호 사이에는 한 칸의 공백을 출력한다.

"""
import sys


def solve(cnt, num):
    ans = []
    for i in range(cnt):
        ans.insert(i-num[i], i+1)
    
    for k in ans:
        print(k, end=" ")

if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    
    solve(cnt, num)