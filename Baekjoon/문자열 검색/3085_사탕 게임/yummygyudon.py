# " 연속한 것이 있는지 확인하고 얼마나 연속되는지 계산하는 함수 " 가 별도로 필요함 (값 위치 바꾸는 작업 XXX)

# 본 계산에서는 행에서 가로로 인접한 것을 교환하고 위 함수를 실행하는 실행문을 각각 붙어있는 같은 행의 인접 쌍(pair)에 대해 모두 반복
#             열에서 세로로 인접한 것을 교환하고 위 함수를 실행하는 실행문을 각각 붙어있는 같은 열의 인접 쌍(pair)에 대해 모두 반복


## 풀이 1 _ 런타임 에러
""""
# 제일 길게 연속되있는 경우의 그 길이 구하는 함수
def check(arr) :
    n = len(arr)
    answer = 1 # 연속된 사탕이 없는 사탕 한개 그 자체의 경우
    for i in range(n) :
        # <같은 행> "가로" 방향으로 확인
        cnt = 1 # 기본값 사탕 1개 그자체
        for j in range(n-1) :
            # 오른쪽 값 지정할 때 j+1
            # n-1 안하면 OutOfArray
            if arr[i][j] == arr[i][j+1] :
                # 오른쪽 값과 동일할 때 == "연속된다"
                cnt += 1
            else :
                # 오른쪽 값과 다르면 == 연속 해제 -> "초기화"
                cnt = 1

            # 지금까지 검사했던 행 중에서 더 길었던 연속값이 있는지 비교
            if answer < cnt :
                answer = cnt # 갱신

        # <같은 열> "세로" 방향으로 확인
        cnt = 1  # 기본값 사탕 1개 그자체
        for j in range(n - 1):
            # 아랫 값 지정할 때 j+1
            # n-1 안하면 OutOfArray
            if arr[j][i] == arr[j+1][i]:
                # 아랫 값과 동일할 때 == "연속된다"
                cnt += 1
            else:
                # 아랫 값과 다르면 == 연속 해제 -> "초기화"
                cnt = 1

            # 지금까지 검사했던 행 중에서 더 길었던 연속값이 있는지 비교
            if answer < cnt:
                answer = cnt  # 갱신
    return answer

import sys
N = int(sys.stdin.readline())
candy = [list(sys.stdin.readline().strip()) for _ in range(N)]

longest = 0
# 판을 바꿀 수 있는 모든 경우 반복
# 행 바꾸기 & 열바꾸기
for i in range(N) :
    for j in range(N) :
        # < 열 바꾸기 >
        if j+1 < N : # 끝 열 범위 넘어가지 않는 경우에만
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] # 바꾸기

            tmp = check(candy)

            if tmp > longest :
                longest = tmp

            # 바꿔놓은 candy 원상복귀
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        # < 행 바꾸기 >
        if i+1 < N :
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]  # 바꾸기

            tmp = check(candy)

            if tmp > longest:
                longest = tmp

            # 바꿔놓은 candy 원상복귀
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]  # 바꾸기

print(longest)
"""

"""
check하는 것을
한 함수에서 모두 하면 런타임 에러가 발생하고
가로 와 세로 각각 나눠서 작업해야 통과가 되는군요..

또 sys.stdin.readline() 메서드를 쓰면 바로 런타임 에러
그리고 리스트 컴프리헨션 또한 런타임 에러 발생합니다.
빈 리스트에 append하는 방법이 더 빠르다고 나오네요.
"""
n = int(input())
candy = []
for _ in range(n):
    colors = list(map(str, input()))
    candy.append(colors)
longest = 1
def width():
    global longest
    for k in range(n):
        cnt = 1
        for l in range(n - 1):
            if candy[k][l] == candy[k][l + 1]:
                cnt += 1
                longest = max(longest, cnt)
            else:
                cnt = 1
def height():
    for k in range(n):
        global longest
        cnt = 1
        for l in range(n - 1):
            if candy[l][k] == candy[l + 1][k]:
                cnt += 1
                longest = max(longest, cnt)
            else:
                cnt = 1
for i in range(n):
    for j in range(n - 1):
        if candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            width()
            height()
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j + 1]
        if candy[j][i] != candy[j + 1][i]:
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            width()
            height()
            candy[j + 1][i], candy[j][i] = candy[j][i], candy[j + 1][i]

print(longest)

### 실패실패
# import sys
# N = int(sys.stdin.readline())
# candy = [list(sys.stdin.readline().strip()) for _ in range(N)]
# longest = 1
#
# def check(arr):
#     global longest
#     for i in range(N):
#         cnt = 1
#         for j in range(N - 1):
#             if arr[i][j] == arr[i][j + 1]:
#                 cnt += 1
#                 longest = max(longest, cnt)
#             else:
#                 cnt = 1
#             if arr[j][i] == arr[j + 1][i]:
#                 cnt += 1
#                 longest = max(longest, cnt)
#             else:
#                 cnt = 1
#
#         # cnt = 1
#         # for j in range(N - 1):
#         #     if candy[j][i] == candy[j + 1][i]:
#         #         cnt += 1
#         #         longest = max(longest, cnt)
#         #     else:
#         #         cnt = 1
# for i in range(N):
#     for j in range(N):
#         if j + 1 < N:
#             candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
#             check(candy)
#             candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
#         if i + 1 < N:
#             candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
#             check(candy)
#             candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
# print(longest)