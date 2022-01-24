# 작성자: red-Pen9uin
# level 10: Recursion
# 2447_별 찍기 - 10
# 수행 결과: 136680 KB / 116 ms (Pypy3)
"""
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N*N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)*(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다.
즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.

"""

# 27의 경우
"""
1. 9*9 정사각형을 크기 9의 패턴으로 둘러쌈
2. 3*3 정사각형을 크기 3의 패턴으로 둘러쌈
필요한 배열: 27*27

Python으로 진행중이므로 list를 적극 활용해서 풀어볼 문제.
C++이었으면 포인터 파티?

- n*n 배열이 만들어짐
- 0, 1, 2,
  3, [], 5,
  6, 7, 8 의 자리에 넣을 n/3의 결과 호출
    - n/3이 1이면 '*'
- 마지막에는 '\n'이 없음~~
- 1, 2, 3 / 6, 7, 8에서는 행끼리 join
- 3, 5 join할 때엔 [] 자리에 [' '*(n/3)] 넣을 것
- 행은 join시킨뒤 [ n*n ] 사이즈 배열 반환

"""

import sys

    
def print_star(N: int) -> str:
    result = list()
    top_bottom = list()
    middle = list()

    if N==1:
        return '*'

    else:
        smaller = print_star(N//3)
        
        for i in range(0, N//3):
            tmp1 = smaller[i] * 3
            top_bottom.append(tmp1)

            tmp2 = smaller[i] + ' '*(N//3) + smaller[i]
            middle.append(tmp2)
        
        result += top_bottom
        result += middle
        result += top_bottom
    
    return result

def print_test(N: int) -> str:
    result = ["*"] * N
    for i in range(len(result)):
        result[i] = result[i]*3

    return result

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(f"\n".join(print_star(num)))