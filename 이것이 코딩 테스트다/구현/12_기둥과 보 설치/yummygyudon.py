def solution(n, build_frame) :
    m = [[0]*(n+1) for _ in range(n+1)] # 바닥 표시용
    for i in range(n+1):
        m[0][i] = 1
    installed = [[0]*(n+1) for _ in range(n+1)] # 기둥 : 1로  보: 2 -> 기둥-보 연결된 부분 : 3
    # 기둥 : 바닥 위(0에서 가능) or 위가 보 한쪽 끝부분 연결(2와 연결되는 경우) or 다른 기둥 위(1일땐 위로만 가능)   "" 가능 ""
    # 보 : 한 쪽 끝이 기둥 연결 or 양 쪽 끝이 다른 보 연결 -> 왼쪽/오른쪽 기둥인지 확인


    is_bottom = [True]*(n+1)

    pt = len(build_frame)
    # only_pillar = True
    for i in range(pt) :
        x, y, a, b = build_frame[i]
        if a == 0 : # 기둥
            if b == 1 : # 설치 할 때
                if m[y][x] == 1 : # 바닥에서 시작할 경우
                    installed[y][x] += 1
                    installed[y+1][x] += 1
                    is_bottom[x] = False
                # 바닥 시작이 아니면
                elif 1 <= installed[y][x] <= 2 : # 다른 기둥에 이어서 세우는 경우 or 보의 끝인 경우
                    installed[y][x] += 1
                    installed[y+1][x] += 1
                else :
                    # print("무시")
                    continue
            else : # 삭제할 때 (밑에 부분의 좌표가 나오는 것을 유의)
                if installed[y+1][x]-1 <=  2 :# 기둥을 삭제했을 때 다른 보와 이어지지도 않은 보의 끝인 2일 경우 불가능
                    # print("무시")
                    continue
                installed[y][x] -= 1
                installed[y+1][x] -= 1
                if y == 0 :
                    is_bottom[x] = True # 다시 그저 바닥으로 변화
        else :  # 보
            if b == 1 : # 설치
                if installed[y][x] == 1 or installed[y][x] == 2  or installed[y][x] == 3:# 기둥 윗부분 / 보 끝에 이어서 설치하는 경우
                    installed[y][x] += 2
                    installed[y][x+1] += 2
                elif  installed[y][x+1] >= 1: # 오른쪽 기둥에서  보 설치하는 경우
                    installed[y][x] += 2
                    installed[y][x + 1] += 2
                else :
                    # print("무시")
                    continue
            else :
                # (기둥 - 보의 경우)   (보-보의 경우) / (오른쪽이
                if 1<= installed[y][x]-2 <=2 or 2 >= installed[y][x+1]-2 >= 1 :
                    # print("무시")
                    continue
                installed[y][x] -= 2
                installed[y][x-1] -= 2
    # print(installed)

    # 시작이 1 이거나 2이면 기둥 <<기둥인 경우>>  //  기둥-보 : 3 이고 보-보 :4 <<보인 경우>>
    result = []
    for i in range(n+1) :
        for k in range(n+1) :
            if i == 0 : # 바닥일 때 (기둥만 가능한 범위)
                if is_bottom[k] == False : # 기둥이 세워져있는 곳
                    result.append([k, i, 0]) # 기둥 정보 추가
            elif installed[i][k] == 2 :
                result.append([k, i, 0])


            elif 3 <= installed[i][k] : # 기둥-보 : 3 이고 보-보 :4 <<보인 경우>>

                if installed[i+1][k] > 0 : # (보 - 기둥 일경우 위 칸까지 0보다 크게됨)
                    # 보-보인 경우로 오른쪽을 봐도 되지만 ouy of range 오류 발생 가능성 있음.
                    result.append([k, i, 0])
                elif installed[i-1][k] >= 1 : # 보의 오른쪽 끝인 상황에서 밑이 기둥일 경우
                    # 기둥이라면 기둥 기준에서 result에 삽입되어야하기 때문에 넘어가기
                    if k == n :
                        continue
                    elif installed[i][k+1] == 0 :
                        continue
                    # (마지막 열이 아니면서 )옆에 보가 이어지는 경우엔 "보(1)" 로 삽입
                    elif installed[i][k+1] >= 3 : # 3인 이유는 다음칸에 바로 기둥으로 올라갈 수 도 있기때문
                        result.append([k, i, 1])
                else :
                    result.append([k, i, 1])
    result.sort() # 결과를 보니 첫번째 값을 기준으로 정렬 되어잇음
    return result


if __name__ == "__main__" :
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    print(solution(n, build_frame))

    m = 5
    build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(solution(m, build_frame2))