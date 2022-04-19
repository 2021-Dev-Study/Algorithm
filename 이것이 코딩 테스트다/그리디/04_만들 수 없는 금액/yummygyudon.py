N = int(input())
coin = list(map(int, input().split()))
coin.sort()

num = 1
all_able = True # 구성되어있는 동전으로 총 값 합 범위의 모든 값이 만들어지면 ex. 1 1 1 1 1 로 1원이 5개 있으면 5원까지 모두 만들어질 수 있으니 최솟값은 6이 되어야함
for c in coin :
    if num < c :
        print(num)
        all_able = False
        break
    num += c
if all_able :
    print(num)

