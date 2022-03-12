if __name__ == "__main__":
    N, M = map(int, input().split())
    balls = list(map(int, input().split()))

    # balls에 같은 무게의 공이 2개 있는 경우가 몇 번인지 세기
    # 중복해서 세기 때문에 나중에 //2를 해야 함
    cnt = 0
    for i in balls:
        if balls.count(i) == 2:
            cnt += 1
    
    # N개의 공에서 2개를 뽑는 순열 - 같은 무게의 공이 2개 있는 경우
    print(N*(N-1)//2-cnt//2)



# N개의 공에서 2개를 뽑는다 -> 순열
# 단 두 사람이 선택한 공의 무게가 같아서는 안된다 -> 같은 무게의 공을 2명이 고르는 경우를 빼준다