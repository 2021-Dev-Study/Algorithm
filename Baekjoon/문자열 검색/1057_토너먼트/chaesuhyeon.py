n, kim, im = map(int, input().split())
cnt = 0
while True:
    if kim == im : # 두 값이 같아지면 그때의 cnt를 세줌
        break
    kim -= kim // 2 # 두명씩 경기를 하니까 2로 나눈 몫을 구해줌
    im -= im // 2 # 두명씩 경기를 하니까 2로 나눈 몫을 구해줌
    cnt += 1

print(cnt)