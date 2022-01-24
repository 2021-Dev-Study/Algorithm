# "남아있는 원반들 중 "가장 밑에 블럭이 목표 기둥으로 가는 과정 -> 함수로
# 이 함수를 재귀로 가장 윗 원반에 도달할 때까지 수행
# 그 과정에서 가장 밑 선반 "위에 있는 선반들"이 중간 기둥을 활용해서 옮겨가는 과정은 모두 "동일함"

# 목표기둥은 단계가 거듭될수록 어차피 남은 원반은 목표기둥에 있는 원반들보다 작은 원반들이기 때문에
# 목표기둥을 활용할 수 있음.

# n = 원반 갯수
# start = 시작하는 기둥
# end = 최종적으로 원반이 옮겨질 기둥
# side = 옮기는 과정에 사용할 중간 기둥

# 3개있을 때의 hanoi -> 2개있을 때의 hanoi -> 1개있을 때의 hanoi(1회) -> 2개있을 때의 hanoi 하단(2회) -> 1개있을 때의 hanoi(3회)
# <맨밑 옮기고 이웃한 곳에 2개 남음> -> 3개있을 때의 hanoi 하단(4회) -> 2개있을 때의 hanoi -> 1개있을 때의 hanoi(5회)
#                                                           -> 2개있을 때의 hanoi 하단(6회) -> 1개있을 때의 hanoi(7회)

## 재귀함수는 종료조건 & 문제 정의를 직관적으로 표현하는 것이 가장 간단함.
def move(start, end) :
    print(f"{start} {end}")

def hanoi (n, start, end) :
    hanoi_subs(n, start, end, 2)

def hanoi_subs (n, start, end, side) :
    if n == 1 : # 종료 조건
        move(start, end)
    else :
        hanoi_subs(n-1, start, side, end) # 시작기둥 원판(맨 밑판이 아닌애들 : n-1 원판) 중간 기둥에 옮기기 (1차 재귀)
        # 다음 순서엔 side였던 기둥이 end기둥 / end 기둥이였던 기둥이 side 기둥
        move(start, end)# 맨 밑판 옮기기
        hanoi_subs(n-1, side, end, start) # 중간 기둥에 있던 원판들 (n-1 원판) 목표 기둥으로 옮기기 (2차 재귀)

n = int(input()) # 원판 개수 입력

print(2**n -1) # 1(1개일때) -> 3(2개일때) -> 7(3개일때) -> 15
hanoi(n,1,3) # 조건이였던 기둥 3개로 시작 1~3 기둥

## 시간 : 896ms / 메모리 : 30860
