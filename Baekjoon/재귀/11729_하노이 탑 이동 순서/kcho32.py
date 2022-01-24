"""
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.
"""

def hanoi(n, start, end):
    ## 기둥 1, 2, 3이라 할 때, 총합에서 시작 수와 끝 수를 빼면 나머지 부분이 나온다고 한다
    empty = 6 - start - end

    if n > 1:
        hanoi(n-1, start, empty)
    answer.append(f'{start} {end}')

    if n > 1:
        hanoi(n-1, empty, end)


answer = []
hanoi(int(input()), 1, 3)
print(len(answer))
print("\n".join(answer))