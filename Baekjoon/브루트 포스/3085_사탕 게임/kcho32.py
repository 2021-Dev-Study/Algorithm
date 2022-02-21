n = int(input())
candy = [list(input()) for i in range(n)]
max_cnt = 1
change = 0

for y_start in range(n):
    for x_start in range(n):
        for i in range(n-x_start):
            if candy[y_start][x_start+i] == candy[y_start][x_start]:
                cnt += 1
                if cnt == n:
                    break
            else:
                if candy[y_start+1][x_start+i] == candy[y_start][x_start] and change == 0:
                    cnt += 1
                    change += 1
                    if cnt == n:
                        break
            
            
    if cnt == n:
        break