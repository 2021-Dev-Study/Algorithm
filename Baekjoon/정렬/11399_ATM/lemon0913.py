# 정렬
# 11399_ATM

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))

    # 입력받은 시간을 오름차순으로 정렬
    lst.sort()

    # 시간합의 최소값 구하기
    # lst = [1, 2, 3, 3, 4] 순서로 줄을 섰을 때 시간의 합을 구하면
    # (1) + (1+2) + (1+2+3) + (1+2+3+3) + (1+2+3+3+4) = 1*5 + 2*4 + 3*3 + 3*2 + 4*1
    sum = 0
    for i in range(len(lst)):
        sum += lst[i] * (len(lst)-i)
    print(sum)