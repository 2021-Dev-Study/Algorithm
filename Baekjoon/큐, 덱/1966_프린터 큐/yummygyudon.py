import sys
case = int(sys.stdin.readline())
for _ in range(case) :
    ea, target = map(int, sys.stdin.readline().rstrip().split())
    importance = list(map(int, sys.stdin.readline().rstrip().split())) # 중요도 나열 리스트
    que = [*enumerate(importance)] # 중요도와 target과 비교할 인덱스 짝지어주기
    cnt = 0
    while True :
        mx = max(importance)
        if que[0][1] == mx :
            cnt += 1 # 출력되는 순서 : 출력될 때만 누적

            if que[0][0] == target : # 찾았다 내 사랑, 내가 찾던 사랑
                print(cnt) # 해당 값이 출력되는 순서가 필요한 것이기 때문에 직전에 누적했던 cnt 그대로 출력
                break
            else :
                que.pop(0) # 최대 중요도이기 때문에 출력되긴해야하니 pop해주기
                importance.pop(0) # 중요도 안빼주면 que에는 없는데 중요도는 많고 뒷값의 중요도가 이전 값 중요도가 될 수 있음.

        else : # 맨 앞 값이 최고중요도 아닌 경우
            que.append(que.pop(0)) # 0번째 빼서 뒤로 추가
            importance.append(importance.pop(0))
