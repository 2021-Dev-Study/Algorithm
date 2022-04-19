# 이번 문제는 무슨말인지를 이해를 못해서 교재를 참고했습니다
from itertools import permutations

def solution(n : int, weak : list, dist : list) :
    # 완탐을 위해 ▶ out of range 오류 발생 해결 (반시계로 돌 수 있기 때문에 넘어가는 값까지)
    #원본 weak의 index값
    length = len(weak)
    for i in range(len(weak)) :
        weak.append(weak[i]+n)
    # 2배의 길이로 원본 값들간의 차이는 그대로인 연장선 생성

    answer = len(dist)+1 # 최솟값을 구하기 위한 초기 비교값 ( 투입가능 최대 인원 + 1 )
    # 원본 weak값들 순서대로
    for start in range(length) :
        for friends in list(permutations(dist, len(dist))) : # 모든 조합
            workers = 1
            pos = weak[start] + friends[workers-1] #처음 투입된 사람이 점검할 수 있는 범위
            #                   (start) (pos)
            #                   (index) (pos)    (if문 pos)
            #                    |--------|→ index 가능 범위
            #                    |        |       |
            # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
            # 1       5 6       10 (1)         (5)(6)
            #                      11          15 16          20
            for index in range(start, start+length) : # 취약점 점검 시작부분 ~ (시작 취약점 기준) 마지막 취약 지점 거리 ( 이부분을 위해서 2배로 늘린 것)
                # 모든 pos가
                if pos < weak[index] :
                    workers += 1
                    if workers > len(dist) : # 투입할 친구가 더이상 없을 경우
                        break
                        # return -1 # 여기서 return을 하면 안되는 이유가 """처음부터 pos가 범위를 넘어갔을 경우"""의 반례가 존재
                    pos = weak[index] + friends[workers -1]
            answer = min(answer, workers)
    if answer > len(dist) :
        return -1
    return answer

if __name__ == "__main__" :
    print(solution(12, [1,5,6,10], [1,2,3,4]))
    print(solution(12, [1,3,4,9,10], [3,5,7]))