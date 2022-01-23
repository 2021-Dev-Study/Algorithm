# 재귀 (단계별 & 실버5)
# 5568_카드 놓기


# 순열의 개념을 사용 -> 재귀로 구현 가능함
# https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations

import sys
from itertools import permutations # 이런거 코테에서 쓸 수 있는지 없는지 어떻게 아시나요??

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    card = [] # 카드에 적혀있는 수 입력받기
    for _ in range (n):
        card.append(int(sys.stdin.readline()))
    
    result = set() # 결과를 담는 집합(집합 -> 중복 제거)
    per = list(permutations(card, k)) # card 배열에서 k개 뽑아서 만든 순열 리스트
    for i in per: # 순열 리스트의 값들로 정수 조합 만들기(중복되는 값은 제거)
        result.add(''.join(list(map(str, i))))
    print(len(result))











# list() 대신 set() 사용시 중복을 걸러줌
# permutations(arr, k) -> arr에서 k개의 원소를 뽑아 순열을 만들어줌
# ''.join(list) -> 리스트에 있는 요소 하나하나를 합쳐 하나의 문자열로 반환 
#                  ex) lst=['a', 'b', 'c']일 때 print(''.join(lst))를 하면 abc를 출력
# list(map(str, x)) -> x를 문자열로 바꾼 리스트를 반환

# --------------------------------------------------------------

# sorted(arr) : arr를 오름차순으로 정렬한 결과를 반환
# sorted(arr, reverse=True) : arr를 내림차순으로 정렬한 결과를 반환

# if not x 의 조건에 들어맞는 x는 다음과 같다.
# 1) False
# 2) 0
# 3) 빈 리스트 [] 
# 4) 빈 튜플 ()
# 5) 빈 딕셔너리 {}
# 6) 문자길이 0의 문자열 ""
# 7) None