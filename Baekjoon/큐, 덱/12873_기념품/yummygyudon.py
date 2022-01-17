
# etc : 지난 반복에서 "삭제된 값 뒤부터 que 끝까지" 남은 값
# 티번호(que 인덱스)
# (*) : "하나" 시작
#                    <que 상태>                           |   <단계_삭제될 번째( [(단계**3)%길이])>      | 삭제 인덱스 ( 삭제번째 - [전체길이 - (이전 과정에서 삭제값 인덱스)] )
# [1(*),2(1),3(2),4(3),5(4),6(5),7(6),8(7),9(8),10(9)]              1 _ 1번째 : index(0)  1%10 : 1           |                 다음 시작 : 2 _아홉번째가 넘어가면 다시 처음으로 넘어감
# 1 [2(*),3(1),4(2),5(3),6(4),7(5),8(6),9(7),10(8)]      |          2 _ 8번째 : index(7)  8%9 :  8           |                 다음 시작 : 10 _첫번째가 넘어가면 다시 처음으로
# [2(0),3(1),4(2),5(3),6(4),7(5),8(6),10(*)]            |           3 _ 27번째: index(2)  27%8 : 3
# [2(0),4(*),5(2),6(3),(4),7(5),8(6),10()]
#delete :

# start index = 6 # len(que) +1 -> 임시
# start 순번 = "하나(1)" 부터 덱처음
# 남은거 = 길이 빼기 전 남은거
# [1,3,4,7,9, 12]
# 길이 6 시작 1 남은거 6
#
#
# 1번째 삭제 => 1번째 1(번째 - 남은거) 삭제 (뒤에 2개 남음 -> [다음 단계]"셋 (3)" 부터 덱 처음) 마지막에서 두번째가 다음 1번째
# [1,3,4,7,9,12] -> [1,4,7,9,12]
# 계산 전 덱 len - 삭제번째
#
# [3,4,7,9,12]
# 길이 5 시작 4 남은거 5
#
# 6번째 삭제 => 1번째 4 (남은거 -번째%길이) 마지막에서
# [1,4,7,9,12] -> [1,7,9,12]
#
# [1,7,9,12]
# 길이 4 시작 7 남은거 3
# 1 -0
# 7번째 삭제 => 4번재 12(번째 - 남은거) 삭제
# [1,7,9,12] -> [1,7,9]
#
# 길이 3 남은거 3
# 5번째 삭제 => 2번째 2 (번째 % 길이 + 남은거)
# [1,2,4]

import sys
n = int(sys.stdin.readline().rstrip())
que = [int(i) for i in range(1,n+1)]
stg = 1
idx = 0
while len(que) > 1 :
    t = (stg**3)
    idx +=  t-1 # 여태까지 세었던 번째수를 모두 누적합 -> 단계마다 다음 순서로 이어지기 때문
    if idx >= len(que) :
        idx = idx%len(que)
    que.pop(idx)
    stg += 1
print(que[0])

while len(que) > 1 :
    t = (stg**3) -1
    idx +=  t
    if idx >= len(que) :
        idx = idx%len(que)
    que.pop(idx)
    stg += 1
print(que[0])

# n = int(sys.stdin.readline().rstrip())
# que = [int(i) for i in range(1,n+1)]
# stg = 1
# idx = 0
# for i in range(n-1) :
#     t = (stg**3)%len(que)
#     idx +=  t-1 # 여태까지 세었던 번째수를 모두 누적합 -> 단계마다 다음 순서로 이어지기 때문
#     if idx >= len(que) :
#         idx = idx%len(que)
#     que.pop(idx)
#     stg += 1
# print(que[0])






# que = [None]*capacity
# stage = 1
# for i in range(capacity):
#     que[i] = i+1
# delete = 0
# etc  = 0 # 10
# while len(que) > 1 :
#     # etc = abs(len(que) - etc)  # 나머지 : 계산 전 _ 10 -10 = 0  | 9 -9 = 0 | 8 - 1 = 7
#
#
#     t = (stage ** 3) # 1 | 8 | 27 | 64
#     print()
#     print(f"{t} 까지 외침")
#
#     delete = t % len(que) # 삭제할 번째  1%10 = 1 | 8%9 = 8 | 27%8 = 3 | 64%7 = 1
#     print(f"{delete} 번째 삭제할 예정")
#     if etc >= delete : #
#         # %나머지 나눌 수가 나눠지는 수보다 클경우 : 나머지는 그대로인 경우 _ 사이클 넘어가지 않는 경우
#
#         pos = delete  # 그냥 번째 수 사용 _ -1은 index 때문 _  8
#         print(f"{t}번째는 이전 반복 이후 사이클을 안넘어서 \n 머리에서부터 {pos}만큼 이동 & 지울 값 도착")
#     else :
#         pos = abs(delete - etc) # 1 - 0 = 1 | 3 - 1 = 2
#         print(f"{t}번째는 이전 반복 이후 사이클을 넘어서 \n 머리에서부터 나머지를 뺀 만큼 {pos} 이동 & 지울 값 도착")
#     etc = abs(len(que) - pos)  # 다음 반복에 필요한 나머지 : 10 - 1 = 9 | 9 - 8 = 1 | 8 - 3 = 5
#     print(f"빼기 전 {etc}개가 뒤에 남음")
#     if pos == len(que) : #
#         real = 0
#         print(f"이전 사이클에 딱 마지막 값에 끝나서 배열 첫 번째값 지움")
#         # etc = abs(len(que) - delete) # 다음 반복에 필요한 나머지 : 6 - 1 : 5 | 5-2 : 3
#
#     else:
#         real = pos-1 # 인덱스 계산 0 | 7 | 2
#         print(f"delete보다 1 작게 해서 지울 값의 배열 주소")
#     stage += 1
#     print(f"'{que[real]}' POP!!!!")
#     que.pop(real)
# print(que)








# while len(que) > 1 :
#     print(f"<{stage} 단계>")
#     print(f"{(stage ** 3)} 까지 외침>")
#     # p = stage ** 3 -1
#     delete = (stage ** 3) % len(que) # 1일 때 delete : 1번째
#     out = delete -1 # 실제 삭제 인덱스 1(0)
#     print("삭제 순번 : ", delete, "번째")
#     if len(que)-delete > 0:
#         que.pop(len(que)-d)
#         d += out + 2
#         print("다음 시작 순서 : ", ptr)
#     else :
#         que.pop(out)
#     print(out+1,"번째 삭제 / 현재 큐 : ", que)
#     print("남은 인원 : ",len(que))
#     print()
#     stage += 1
#     etc =



