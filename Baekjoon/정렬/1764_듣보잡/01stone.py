# 1764 : 듣보잡
'''
첫째 줄 : 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
둘째 줄 : N개의 줄에 걸쳐 듣도 못한 사람의 이름과, 
          N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어짐

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성
'''
# 교집합 이용 : set

n, m = map(int, input().split())

n_set = set()
for _ in range(n):
  n_set.add(input())

m_set = set()
for _ in range(m):
  m_set.add(input())

n_and_m = sorted(list(n_set & m_set))

print(len(n_and_m))
for i in n_and_m:
    print(i)


'''
# 맞힌 사람 코드
import sys

n, m = map(int, input().split())

nameList = sys.stdin.read().splitlines()

hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()

print(len(ret))
for i in ret:
    print(i)
'''