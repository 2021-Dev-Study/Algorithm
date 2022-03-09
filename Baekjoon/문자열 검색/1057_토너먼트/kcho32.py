round, x, y = map(int, input().split(" "))
cnt = 0
done = False

if x > y:
        x, y = y, x

while round >= 2:
    cnt += 1

    if x % 2 and y == x + 1:
        print(cnt)
        done = True
        break
    
    if x % 2:
        x = x // 2 + 1
    else:
        x = x // 2

    if y % 2:
        y = y // 2 + 1
    else:
        y = y // 2
    if round % 2:
        round = round // 2 + 1
    else:
        round //= 2
    

if not done:
    print("-1")