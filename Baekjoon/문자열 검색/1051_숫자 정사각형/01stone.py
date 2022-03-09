# 1051 : 숫자 정사각형

n, m = map(int, input().split())
rectangle = [list(map(int, input())) for _ in range(n)]
rect_range = min(n, m)

answer = 0
for x in range(n):
  for y in range(m):               # x, y 범위~ 일단 모든 꼭짓점에 접근할 수 있어야 함..
    for z in range(rect_range):    # 정사각형 크기 조절 
      if (x+z) < n and (y+z) < m:  # 인덱스에러 피하려면 조건 정해줘야 함
        if (rectangle[x][y] == rectangle[x+z][y] == rectangle[x][y+z] == rectangle[x+z][y+z]):  # 꼭짓점이 동일하면
          answer = max(answer, (z+1)**2)                                                        # 큰 값 넣기

print(answer)