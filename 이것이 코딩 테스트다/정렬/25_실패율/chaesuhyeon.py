def solution(n, stage):
    answer = []
    cnt = len(stage)
    i = 1
    arr= []
    result = 0
    while i <= n: # i가 n보다 작거나 같을 동안에만 반복 수행
        for j in range(len(stage)): # stage와 같은 숫자가 리스트 안에 있으면 개수(result)추가
            if stage[j] == i:
                result += 1

        arr.append((i, result/cnt)) # arr 리스트에 stage와 실패율 추가
        
        if cnt > result: # cnt가 음수값이 나오면 안되므로 조건문 써서 처리 (안쓰면 런타임 에러 발생)
            cnt -= result # 남은 인원수 - 통과 못한 사람의 수

        result = 0 # result 초기화
        i += 1 # stage += 1

    arr.sort(key = lambda x : -x[1]) # 실패율 내림차순
    answer = [i[0] for i in arr] # stage만 뽑음
    return answer


