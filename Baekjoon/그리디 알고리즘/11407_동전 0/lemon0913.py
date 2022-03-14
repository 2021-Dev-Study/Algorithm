# 단계별 - 그리디 알고리즘
# 11047_동전 0
import sys
if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = []
    for i in range(N):
        coins.append(int(sys.stdin.readline()))
    # 동전을 내림차순으로 정렬
    coins.sort(reverse=True)

    #동전의 단위가 큰 순서대로 나누기
    cnt = 0
    for i in coins:
        if i <= K: # 동전의 단위가 금액보다 작거나 같으면
            cnt += K // i # 금액을 동전으로 나눈 몫을 더하기
            K %= i # 금액을 동전으로 나눈 나머지로 수정
        if K == 0: # 연산 과정에서 금액이 0이 되면 반복문 탈출
            break
    print(cnt)
