from itertools import combinations
if __name__ == "__main__":
    N = int(input())
    coins = list(map(int, input().split()))

    # coins로 만들 수 있는 모든 금액 구하기 -> 순열 사용
    # 5개의 동전이 있다면 5C1, 5C2, 5C3, 5C4, 5C5의 경우를 모두 구해서 더하기
    coins_com = []
    for i in range(N):
        coins_com += list(combinations(coins, i+1))
    
    # 순열을 모두 구했다면 sum() 사용해 금액 구하기
    for i in range(len(coins_com)):
        coins_com[i] = sum(coins_com[i])

    # coins_com에 없는 금액이라면 출력하기
    for i in range(1, sum(coins)):
        if i not in coins_com:
            print(i)
