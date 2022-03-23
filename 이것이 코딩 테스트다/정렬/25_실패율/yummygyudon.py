# 도달햇지만 클리어하지 못한 플레이어 수 / 스테이지 도달 플레이어 수

def solution(N, stages) :
    '''
    정확성: 66.7
    합계: 66.7 / 100.0
    '''
    # fail_rate = [[0, i] for i in range(N+1)]
    # stages.sort()
    # cnt = len(stages)
    # for n in range(1, N+1) :
    #     f_players = 0
    #     for s in stages :
    #         if s == n :
    #             f_players += 1
    #         # elif n > s :
    #     if f_players <= 0 :
    #         fail_rate[n][0] = cnt
    #     else :
    #         fail_rate[n][0] = 1 - (f_players / cnt)
    #     cnt -= f_players
    # fail_rate.sort(key = lambda x : (x[0],x[1]))
    # result = []
    # for _, s in fail_rate :
    #     result.append(s)
    # return result[1:]
    result =[]
    players = len(stages)
    for i in range(1, N+1) :
        p = stages.count(i)
        if players > 0 :
            fail_rate = p / players
        else :
            fail_rate = 0
        result.append([1 - fail_rate, i])
        players -= p
    result.sort(key = lambda x : x[0])
    for i in range(len(result)) :
        result[i] = result[i][1]
    return result



if __name__ == "__main__" :
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))

    M = 4
    stages2 = [4, 4, 4, 4, 4]
    print(solution(M, stages2))