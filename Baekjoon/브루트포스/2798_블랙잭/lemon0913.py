# 브루트포스
# 2798_블랙잭

from itertools import combinations
if __name__ == "__main__":
    # N, M, 양의 정수 카드들 입력 받기
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    # 입력받은 카드 리스트에서 3장을 뽑는 조합
    # 뽑은 카드들의 합 구하기
    com_cards = list(combinations(cards, 3))
    for i in range(len(com_cards)):
        com_cards[i] = sum(com_cards[i])
    
    # 카드의 합을 내림차순으로 정렬
    # 정렬된 결과 중 M보다 작거나 같은 수 중에서 제일 큰 수 출력
    com_cards.sort(reverse=True)
    for i in range(len(com_cards)):
        if com_cards[i] <= M:
            print(com_cards[i])
            break

