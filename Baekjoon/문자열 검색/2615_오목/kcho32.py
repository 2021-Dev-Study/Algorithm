board = [list(map(int, input().split(" "))) for i in range(19)]
x, y = 0, 0

for y_start in range(19):
    for x_start in range(19):
        win_cnt = 0        
        if board[y_start][x_start]:
            if x_start <= 14:
                for hor in range(5):
                    if board[y_start][x_start+hor] == board[y_start][x_start]:
                        win_cnt += 1
                    else:
                        win_cnt = 0
                        break
                if x_start <= 13:
                    if win_cnt == 5:
                        if board[y_start][x_start+5] == board[y_start][x_start] and board[y_start][x_start-1] == board[y_start][x_start]:
                            win_cnt = 0
                            break
                        else:
                            x, y = x_start + 1, y_start + 1
                            break
            if y_start <= 14:
                for ver in range(5):
                    if board[y_start+ver][x_start] == board[y_start][x_start]:
                        win_cnt += 1
                    else:
                        win_cnt = 0
                        break
                if y_start <= 13:
                    if win_cnt == 5:
                        if board[y_start+5][x_start] == board[y_start][x_start]:
                            win_cnt = 0
                            break
                        else:
                            if win_cnt == 5:
                                x, y = x_start + 1, y_start + 1
                                break
            if x_start <= 14 and y_start <= 14:
                for right_d_dia in range(5):
                    if board[y_start+right_d_dia][x_start+right_d_dia] == board[y_start][x_start]:
                        win_cnt += 1
                    else:
                        win_cnt = 0
                        break
                if x_start <= 13 and y_start <= 13:
                    if win_cnt == 5:
                        if board[y_start+5][x_start+5] == board[y_start][x_start]:
                            win_cnt = 0
                            break
                        else:
                            if win_cnt == 5:
                                x, y = x_start + 1, y_start + 1
                                break
            if x_start <= 14 and y_start >= 4:
                for right_u_dia in range(5):
                    if board[y_start-right_d_dia][x_start+right_d_dia] == board[y_start][x_start]:
                        win_cnt += 1
                    else:
                        win_cnt = 0
                        break
                if x_start <= 13 and y_start >= 5:
                    if win_cnt == 5:
                        if board[y_start-5][x_start+5] == board[y_start][x_start]:
                            win_cnt = 0
                            break
                        else:
                            if win_cnt == 5:
                                x, y = x_start + 1, y_start + 1
                                break
        else:
            continue
        if win_cnt == 5:
            break
    if win_cnt == 5:
        print(board[y_start][x_start])
        print(y, x)
        break