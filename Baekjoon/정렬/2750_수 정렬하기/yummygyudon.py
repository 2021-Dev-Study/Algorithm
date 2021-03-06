# 시간복잡도가 단순 정렬보단 빠르고 아직 퀵 정렬을 공부 안한 상태여서
# 쉘 정렬 사용했습니당
# 메모리 : 30864KB / 시간 : 72ms
def shell_sort(x : list) :
    n = len(x)
    h = 1

    # 너무 길고 안섞일 경우 대비
    # 9개 미만 길이는 h = 1
    # 몫이 2 이상으로 커질 경우 ( 18개 이상 ) -> 4
    while h < n//9 :
        h = h*3 +1

    # 무조건 마지막 한번은 h=1
    while h>0 :
        # ex. 8개가 있을 때

        # <마지막 h= 1>
        # h = 1, n = 8
        # j는  0 - 1 - 2 - 3 ...
        # 왼쪽부터 이웃한 숫자들끼리 반복때마다 오른쪽->왼쪽 방향으로 비교해나가는 방식
        #
        # 첫 반복문 j =0, tmp = x[1]
        #   첫번째 값이 두번째 값(tmp)과 같거나 작으면
        #       x[1] = tmp : 그대로
        #   첫번째 값이 두번째 값(tmp)보다 크면
        #       위치 치환
        #       x[1] = x[0]
        #
        # 두 반복문 j = 1, tmp = x[2]
        #   두번째 값이 세번째 값(tmp)과 같거나 작으면
        #       x[2] = tmp : 그대로
        #   [ 두번째 값 > 세번째 값(tmp) ] -> [ 첫번째 값 > 세번째 값(tmp) ]
        #       위치 치환
        #       x[2] = x[1] : 앞에있던 값이 뒤로 옮겨짊
        #       x[1] = x[0] : 그 다음 앞에 있던 값이 뒤로 옮겨짐
        #       x[-1+1] = tmp : 첫 자리로 오게됨.

        # 이런 방식으로 진행됨.

        for i in range(h, n) :
            # 생기는 집합 갯수만큼 반복
            j = i - h # 초기값은 무조건 0 (배열 첫번째 값) -> 순차적으로 오른쪽 값
            tmp = x[i] # 일정한 간격으로 떨어져 있는 값을 tmp에 저장 _ (h+1), (h+

            while j >= 0 and x[j] > tmp :
                # 만일의 경우 왼쪽까지 모두 싹 훓을 수 있고
                # 떨어져 있는 값과
                x[j+h] = x[j]
                j -= h
            # 만약 앞에 있는 값이 떨어져있는 값 x[i] 작으면
            x[j+h] = tmp

        h = h//3

import sys
N = int(sys.stdin.readline())
a = []
for _ in range(N) :
    a.append(int(sys.stdin.readline()))

shell_sort(a)

for num in a :
    print(num)