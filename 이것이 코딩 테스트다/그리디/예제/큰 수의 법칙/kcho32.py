'''
입력 조건: 
1. 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수, 공백으로 구분
2. 둘째 줄에 N개의 자연수, 공백으로 구분, 자연수는 1 이상 10000 이하
3. K <= M

출력 조건:
1. 큰 수의 법칙에 따라 더해진 답 출력
'''

# N개의 자연수 중 서로 같은 것이 존재하다면 K개 보다 더 많이 출력 가능
# N은 주어진 자연수의 갯수
# M은 숫자가 더해지는 횟수
# K는 주어진 자연수 중 하나가 더해질 수 있는 최대 횟수

import sys

# N, M, K에 키보드로 입력받은 값들을 대입 해준다.
N, M, K = map(int, sys.stdin.readline().rstrip().split(" "))

nums: list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# 입력 받은 자연수들을 크기 순으로 정렬
nums.sort()
answer = 0

while M:
    count = K
    max_num = nums.pop()
    
    while count:
        answer += max_num
        count -= 1
        if not M:
            break
        M -= 1

        print(M, K, answer)
    

print(answer)