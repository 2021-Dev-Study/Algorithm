def solution(n, build_frame):
    def init(n):
        res = []
        for i in range(n + 1):
            temp = []
            for j in range(n + 1):
                temp.append([j, i, 0, 0])
            res.append(temp)
        return res

    def check(now_block, x, y):
        res = True
        if now_block[y][x][2] == 1:  # 기둥
            if y == 0 or now_block[y - 1][x][2] == 1 or now_block[y][x][3] == 1 or (
                    x > 0 and now_block[y][x - 1][3] == 1):
                res = True
            else:
                return False
        if now_block[y][x][3] == 1:  # 보
            if (y > 0 and now_block[y - 1][x][2] == 1) or (y > 0 and x < n and now_block[y - 1][x + 1][2] == 1) \
                    or (x > 0 and x < n and now_block[y][x - 1][3] == 1 and now_block[y][x + 1][3] == 1):
                res = True
            else:
                return False
        return res

    block = init(n)
    # build_frame: (가로, 세로, 종류, 설치여부)
    for k in range(len(build_frame)):
        build = build_frame[k]
        x, y = build[0], build[1]
        typ, act = build[2], build[3]
        if act == 1: # 설치
            if typ == 0:  # 기둥
                block[y][x][2] = block[y][x][2] + 1
                if check(block, x, y) is False:
                    block[y][x][2] = block[y][x][2] - 1
            else:  # 보
                block[y][x][3] = block[y][x][3] + 1
                if check(block, x, y) is False:
                    block[y][x][3] = block[y][x][3] - 1
        else:  # act == 0 삭제
            if typ == 0:  # 기둥
                if block[y][x][2] > 0:
                    block[y][x][2] = block[y][x][2] - 1
                    if (check(block, x, y) and check(block, x, y + 1) and check(block, x - 1, y + 1)) is False:
                        block[y][x][2] = block[y][x][2] + 1
            else:  # 보
                if block[y][x][3] > 0:
                    block[y][x][3] = block[y][x][3] - 1
                    if (check(block, x, y) and check(block, x - 1, y) and check(block, x + 1, y)) is False:
                        block[y][x][3] = block[y][x][3] + 1

    #     return block (출력 형식에 맞게)
    # answer: (가로, 세로, 종류)
    answer = []
    for i in range(len(block)):
        for j in range(len(block)):
            if block[j][i][2] > 0:
                answer.append([block[j][i][0], block[j][i][1], block[j][i][2] - 1])
            if block[j][i][3] > 0:
                answer.append([block[j][i][0], block[j][i][1], block[j][i][3]])
    return answer