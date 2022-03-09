import sys

n: int = int(sys.stdin.readline().rstrip())

# 리스트에 덩치(몸무게, 키)를 튜플로 받고, 해당 값들을 딕셔너리에 넣어준다 (1로 초기화)
## 튜플 -> 리스트 : 튜플로 받을 시, 같은 몸무게, 키를 가진 경우 에러 발생
body: list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(n)]
body_cnt: list = [1 for i in range(n)]

# 브루트 포스를 통해 1, 2 / 1, 3 / 1, 4 ... 2, 3/ 2, 4 ... 3, 4 / .. 이런 식으로 겹치지 않는 모든 경우를 비교해준다.
# 비교시 덩치가 작은 쪽의 인덱스의 값(value)에 1을 더해주어 순위를 뒤로 더해준다.
for i in range(n-1):
    for j in range(i+1, n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            body_cnt[i] += 1
        elif body[i][0] > body[j][0] and body[i][1] > body[j][1]:
            body_cnt[j] += 1

for i in range(n):
    print(body_cnt[i], end=" ")