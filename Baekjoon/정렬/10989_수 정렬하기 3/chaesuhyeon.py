# 10989 수 정렬하기3
# pypy3 
# 메모리 초과
# for문 속에서 append를 사용하면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용 하지 못함
import sys
N = int(sys.stdin.readline().rstrip())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()
for i in range(len(num)):
    print(num[i])

# 재풀이
# python    
# 파이썬은 내부적으로 연산과 메모리를 관리하기 때문에 파이썬에 내장되어 있는 함수를 적용할 수록 메모리를 효율적으로 관리
# https://wikidocs.net/21057 참고 
# 입력값이 10000개까지 주어질 수 있는데 인덱스는 0부터 시작하므로 10001인 리스트 만듦
import sys
N = int(sys.stdin.readline())
num_list = [0] * 10001 # 리스트에 각 요소마다 0을 할당
for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1 # 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해줌 

for i in range(10001):
    if num_list[i] != 0: # num_list[i]값이 0이 아니면
        for j in range(num_list[i]): # 값이 0이 아닌 것의 인덱스를 출력 
            print(i)