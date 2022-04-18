if __name__ == "__main__":
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))

    start = 0
    end = max(tree)

    result = 0
    while start <= end:
        mid = (start+end)//2  #자르는 기준

        total = 0
        for i in tree:
            if i > mid: # 나무가 자르는 기준보다 큰 경우
                total += i-mid # 자른 뒤, 잘린 부분의 길이 합 구하기
       
        if total < M: # 잘린 부분의 길이 합이 목표치보다 작은 경우
            end = mid-1 # 자르는 기준을 줄이기
        else: # 잘린 부분의 길이 합이 목표치보다 크거나 같은 경우
            start = mid + 1 # 자르는 기준 키우기
            result = mid # 일단 답이 될 수 있으니 result에 저장하기

    print(result)


# 완전 동일한 코드를 제출했을 때 한번은 시간 초과, 한번은 정답......
# 뭐가 문제인건가요..???




