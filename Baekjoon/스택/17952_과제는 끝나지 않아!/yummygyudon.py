import sys
n = int(sys.stdin.readline())
score = 0
limit = 0
for i in range(n,0,-1) :
    s = list(input().split())
    if int(s[0]) == 1 : # 첫자리가 1일 경우 -> 새로운 과제가 주어지는 경우
        if limit > 0 : # 이전 과제 안끝났을 때
            if int(s[2]) == 1 : # 근데 1분짜리 과제일 때
                score += int(s[1]) # 1분짜리라면 그자리에서 끝내기때문에 이어서 할 수 있게끔 점수만 누적합
            else :
                score = int(s[1]) # 초기화
                limit =(int(s[2])-1) # 초기화하고 새로운 과제 limit 대입 _ 바로 1 차감이니까 -1
        elif limit == 0 :
            if (int(s[2])-1) > n : # 남은 분보다 limit이 더 큰 경우 해당 과제는 끝날때까지 불가능
                continue
            else:
                score += int(s[1]) # 이전과제이거나 새롭게 시작할 경우 -> 점수 누적합
                limit = (int(s[2])-1) # 초기화 하고 새로운 과제 limit 대입
        else :
            score = score + int(s[1])
            limit = (int(s[2]) - 1)
    else :
        if limit > 0 :
            limit -= 1 # limit 1 감소
        else :
            continue #

print(score)