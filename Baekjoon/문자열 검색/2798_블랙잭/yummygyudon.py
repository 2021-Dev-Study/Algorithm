import sys
N, M = map(int,sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0
# 앞에서부터 첫번째 픽으로 사용하게 되면 끝에 두개는 첫번째 픽으로 올 수 없음
for i in range(N-2): # 원래 N보다 2가 작아야하지만
    f_pick = cards[i]
    for k in range(i+1, N) :
        s_pick = cards[k]
        for j in range(k+1, N) :
            t_pick = cards[j]
            sum = f_pick + s_pick + t_pick
            v = M-(sum)
            if v >= 0 :
                result = max(result, sum)
            else :
                continue
print(result)



# print(ls)