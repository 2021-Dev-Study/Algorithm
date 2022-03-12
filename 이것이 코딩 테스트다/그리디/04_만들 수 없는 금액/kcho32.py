n = int(input())
money = sorted(list(map(int, input().split())), reverse=True)
goal = 1
answer = 0

while True:
    if answer != 0:
        break
    
    tmp = goal
    
    for i in money:
        if i > tmp:
            continue
        else:
            tmp -= i

    if tmp:
        answer = goal
    else:
        goal += 1

print(goal)