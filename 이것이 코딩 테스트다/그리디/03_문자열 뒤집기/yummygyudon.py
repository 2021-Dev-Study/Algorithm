S = list(input())
start = S[0]
status = False
cnt = 0
for i in range(1, len(S)) :
    if S[i] != start and status == False :
        status = True
        cnt += 1
    elif S[i] == start and status == True :
        status = False
print(cnt)
