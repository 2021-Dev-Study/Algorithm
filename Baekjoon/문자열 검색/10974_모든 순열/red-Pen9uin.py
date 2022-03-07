# 작성자: red-Pen9uin
# Classification: string search
# 10974_모든 순열
# 수행 결과:  KB /  ms
"""
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

"""
import sys
import itertools


def solve(num):
    inp_list = [i for i in range(1, num+1)]
    cnt = 1
    for i in range(1, num+1):
        cnt = cnt*i

    permut_list = list(itertools.permutations(inp_list))
    permut_list.sort()

    for i in permut_list:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    solve(num)