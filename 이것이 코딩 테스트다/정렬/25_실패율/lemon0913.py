# 실패, 런타임 에러
# def solution(N, stages):
#     answer = []
    
#     dic = {}
#     for i in range(1, N+1):
#         n = stages.count(i)
#         dic[i] = n/len(stages)
#         while i in stages:
#             stages.remove(i)
#     answer = sorted(dic.items(), key = lambda x:-x[1])
    
#     for i in range(len(answer)):
#         answer[i] = answer[i][0]
#     return answer

# remove, dictionary 안쓰기 
def solution(N, stages):
    answer = [0] * N
    
    l = len(stages)
    for i in range(1, N+1):
        n = stages.count(i)
        
        if l == 0:
            fail = 0
        else:
            fail = n/l
        answer[i-1] = [i, fail]
        l -= n
    
    answer.sort(key = lambda x:-x[1])
    return [i[0] for i in answer]