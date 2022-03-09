P, kim, lim = map(int, input().split())
cnt = 0
# 궁금한 것 : 특정 번째수들끼리 만날 때까지의 "라운드 수"
# 선수 번호가 아닌 번호가 소속될 "라운드 수"에 집중해야함.

# 1,2번은 "1라운드" 참가
# 1-(1//2) , 2-(2//2) = 1
# 3,4번은 "2라운드"참가
# 3-(3//2) , 4-(4//2) = 2
# 1, 9 번은
# 1, 5라운드 -> 1(1번소속),2,3,4,5(9번 소속) 라운드 진행 = 1단계 결과
# 다시 1번소속의 1라운드 - 2라운드
# 1, 5번의 입장으로 재계산
# 1, 3 라운드
# 1(1번소속),2,3(부전승_9번소속) -> 2단계 결과
# 1, 2 -> 3단계 결과  => 4라운드에 붙게됨

# 2로 나눈 몫을 빼주면 => 매치번째 수
# 서로 만난다는 것 = 매치번째수가 같다는 것
while kim != lim :
    kim -= kim//2
    lim -= lim//2
    cnt += 1 # 단계 완료
print(cnt)



# klmatch = [kim,lim]
# total = []
# kim과 lim의 매치업 리스트가 나올 때까지 모든 매치의 경우의 수를 tmp에 삽입하면서
# 희망 매치업과 같은지 확인하고 그 때까지 1씩 누적합 햇던 cnt를 출력하는 방식을 생각했지만
# 어느쪽이 이겨서 올라갈지 복불복이고 그에 대한 해결방법이 생각이 나지 않아 실패했습니다...
# def match(arr) :
#     global cnt
#     if len(arr)%2 == 0 :
#         tmp =[]
#         for i in range(len(arr),2) :
#             cnt+=1
#             if [arr[i], arr[i + 1]] == klmatch :
#                 print(cnt)
#                 break
#             else :
#                 tmp.append([arr[i], arr[i + 1]])
#     else :
#         tmp = []
#         for i in range(len(arr)-1,2) :
#             cnt += 1
#             if [arr[i], arr[i + 1]] == klmatch:
#                 print(cnt)
#                 break
#             else:
#                 tmp.append([arr[i], arr[i + 1]])
#         cnt += 1
#         tmp.append([arr[len(arr)]])
#     return tmp
# arr = list(range(1,P+1))
# print(arr)
# print(match(arr))