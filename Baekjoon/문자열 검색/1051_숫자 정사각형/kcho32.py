rows, cols = map(int, input().split(" "))
nums = [list(map(int, list(input()))) for i in range(rows)]
answer = 1

# (0, 0)부터 시작점 부여 후 x축, y축 순으로 루프 돌리면서 시작점 옮김
for y_start in range(rows):
    for x_start in range(cols):
        # 시작점에서부터 1씩 움직이면서 같은 수 찾고, 찾았다면 해당 거리만큼의 각 꼭지점 값들이 같은지 확인
        # 꼭지점 값들이 같고 (i + 1)^2가 저장되어 있는 수보다 크다면 저장
        # 시작점이 아래 오른쪽 끝이 될때까지 반복
        for i in range(cols-x_start):
            if nums[y_start][x_start+i] == nums[y_start][x_start]:
                if i > rows - (y_start+1):
                    continue
                else:
                    if (nums[y_start+i][x_start] == nums[y_start][x_start]
                        and nums[y_start+i][x_start+i] == nums[y_start][x_start]):
                        if answer < (i+1) * (i+1):
                            answer = (i+1) * (i+1)

print(answer)