# 정렬
# 1026_보물

if __name__ == "__main__":
    N = int(input())
    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))

    # listA를 오름차순으로 정렬
    listA.sort()

    # listA의 최소값과 listB의 최대값의 곱을 sum에 더하기
    sum = 0
    for i in listA:
        maxB = max(listB)
        sum += i * maxB
        # 한번 사용한 listB의 최대값은 다시 사용하지 않게 -1로 바꿔버리기
        listB[listB.index(maxB)] = -1 
    print(sum)
     