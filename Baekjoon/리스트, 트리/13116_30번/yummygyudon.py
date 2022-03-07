TC = int(input())
# 부모노드 값은 각 자식들을 2로 나눈 후의 정수값인 특징
for _ in range(TC) :
    a, b = map(int, input().split())
    while True :
        # //2 로 하면 틀리는 이유를 모르겠습니다..
        #
        # 부모노드를 비교하는 것이기 때문에 a//2 와 b//2 를 비교하는게 맞다고 생각하는데..
        # a와 b간의 크기비교가 맞고
        # 2로 나눈 정수몫 간의 크기 비교는 왜 틀린것인지...
        # if a//2 == b//2 :
        #     print((a//2) * 10)
        #     break
        # if a//2 > b//2 :
        #     a //= 2
        # elif a//2 < b//2 :
        #     b //= 2
        if a//2 == b//2 :
            print((a//2) * 10)
            break
        if a//2 > b//2 :
            a //= 2
        elif a//2 < b//2 :
            b //= 2