# 첫줄부터 검사
# 이전 for문에서 검사했던 돌이 포함된 밑에 나올 돌의 갯수 계산 때 또 오목인 것으로 나오기 때문에 sys.exit(0)로 바로 종료
import sys

omok = []
for i in range(19):
    omok.append(list(map(int, sys.stdin.readline().split())))

# → ↓ ↘ ↗
# ([dx_높이이동] , [dy_너비이동])
# (0,1) : → / (1,0) : ↓ / (1,1) : ↘ / (-1,1) : ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if omok[x][y] != 0:
            focus = omok[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == focus:
                    # 각각의 이동범위가 19x19 범위 내부일 때만 & 이동해서 확인할 돌이 지정 돌과 같은 값일 때만
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        # 중심 돌(지정 돌)이 봤던 각 방향들의 "반대(-dx[i] & -dy[i])" 방향으로 한 칸씩 확인
                        # 값이 같으면 그 줄은 6개 이상이라는 것

                        # 한개씩만 더보면 6개인지 5개에서 끝나는 지 알 수 있기때문에
                        # 밑에 줄로 내려가서 검사 중에 이전에 검사했던 돌이 세어지더라도 상관 없음
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and omok[x - dx[i]][y - dy[i]] == focus:
                            break # 다시 for문 도세요~
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and omok[nx + dx[i]][ny + dy[i]] == focus:
                            break # 다시 for문 도세요~

                        # 육목이 아니면 성공한거니까 종료
                        print(focus)
                        print(x + 1, y + 1) # index 값이니 1씩 더해주기
                        sys.exit(0) # 발견하는 즉시, for문 자체 종료

                    # cnt가 아직 5개 이상이 안되었을 때
                    nx += dx[i]
                    ny += dy[i]

print(0)

# <<개인 도전>>
# 오목까진 되었으나
# 육목의 경우까진 성공못함

# 개선점 1 : 0 출력하기
# 개선점 2 : sys.exit(0) 활용해서 위에서부터 하나라도 찾았을 때 바로 종료가능하게 하기
# 개선점 3 : 6개인지 까지만 확인하면 됨.

# 삭제했지만 omok[i][k] != '0' 로 통합하고
        #  case들 구하는 것 까지는 공통으로 하고 마지막에 omok[i][k] == '1'과 else로 나눠 코드 단축은 해보았음
# state = False
#
# for i in range(19) :
#     if state :
#         break
#     else :
#         for k in range(19) :
#             if omok[i][k] == '1' :
#                 case1, case2, case3, case4 = [],[],[],[]
#                 for b in omok[i][k:] :
#                     case1.append(b)
#                 for a in range(i, 19) :
#                     case2.append(omok[a][k])
#                 h, w = i, k
#                 while True :
#                     if h > 18 or w > 18 :
#                         break
#                     case3.append(omok[h][w]) # 2, 1 / 3,2 / 4,3 /... 18, 17
#                     h += 1
#                     w += 1
#                 cnt1, cnt2, cnt3, cnt4 = case1.count('1'), case2.count('1'), case3.count('1'), case4.count('1')
#                 if cnt1 == 5 or cnt2 == 5 or cnt3 == 5 :
#                     print(f"1\n{i+1} {k+1}")
#                     state = True
#                     break
#                 elif cnt4 == 5 :
#                     print('1')
#                     print(f"1\n{i+4+1} {k-4+1}")
#                     state = True
#                     break
#
#             elif omok[i][k] == '2' :
#                 case1, case2, case3, case4 = [],[],[],[]
#                 for b in omok[i][k:]:
#                     case1.append(b)
#                 for a in range(i, 19):
#                     case2.append(omok[a][k])
#                 h, w = i, k
#                 while True:
#                     if h > 18 or w > 18:
#                         break
#                     case3.append(omok[h][w])  # 3, 2 / 4,3 / 5, 4
#                     h += 1
#                     w += 1
#                 cnt1, cnt2, cnt3, cnt4 = case1.count('2'), case2.count('2'), case3.count('2'), case4.count('2')
#
#                 if cnt1 == 5 or cnt2 == 5 or cnt3 == 5:
#                     print(f"2\n{i+1} {k+1}")
#                     state = True
#                     break
#                 elif cnt4 == 5 :
#                     print(f"2\n{i+4+1} {k-4+1}")
#                     state = True
#                     break