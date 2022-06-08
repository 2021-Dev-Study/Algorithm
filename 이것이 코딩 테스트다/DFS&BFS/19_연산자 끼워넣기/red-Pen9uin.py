# 작성자: red-Pen9uin
# 작성일: 2022-06-07
# Classification: DFS&BFS algorithm
# 참고: https://velog.io/@yesterdaykite/DFSBFS-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0

import sys
input = sys.stdin.readline

n = int(input())
# 연산 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 갯수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# DFS 메서드
def dfs(i, now) :
	global min_value, max_value, add, sub, mul, div
	# 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
	if i == n :
		min_value = min(min_value, now)
		max_value = max(max_value, now)
	# 아닌 경우, 각 연산자에 대하여 재귀적으로 수행
	else :
		if add > 0 :
			add -= 1
			dfs(i+1, now+data[i])
			add += 1
		if sub > 0 :
			sub -= 1
			dfs(i+1, now-data[i])
			sub += 1
		if mul > 0 :
			mul -= 1
			dfs(i+1, now*data[i])
			mul += 1
		if div > 0 :
			div -= 1
			dfs(i+1, int(now/data[i])) # 나눌때 나머지 제거
			div += 1

dfs(1, data[0])

print(max_value)
print(min_value)