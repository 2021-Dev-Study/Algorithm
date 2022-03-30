s = input()

def solution(s):
    answer = []
    mid = len(s) // 2 # 문자열 나눌 수 있는 최대 개수가 문자열 개수의 반이라서 문자열 중간길이 구해줌
    if len(s) == 1:
        return 1
    for unit in range(1, mid+1): # 단위 1개부터 시작 ~ 문자열길이 반까지 포함해야하므로 +1해줌
        pre = s[:unit] # 처음부터 단위개수만큼 문자추출
        cnt = 1 # 초기값 1개부터 시작
        string = "" # 문자열 더해주기 위해 선언
        for j in range(unit, len(s), unit):
            if pre == s[j:j+unit]: # 단위만큼 뽑은 문자열이 이전 문자열과 같다면 cnt 늘려주기 
                cnt += 1
            else: # 다르다면 다른 문자열이 나왔다는 뜻
                if cnt != 1: # cnt가 1이 아니라면 개수+ 이전 문자열 더해주기
                    string += str(cnt) + pre
                else: # 1이라면 개수를 적어줄 필요가 없으므로 이전 문자열만 더해주기
                    string += pre
                pre = s[j:j+unit] # 새로운 문자열이 나왔으므로 이것으로 비교를 해야하기 때문에 pre를 바꿔줌
                cnt = 1 # cnt도 다시 1로 초기화 
        if cnt != 1:
            string += str(cnt) + pre
        else:
            string += pre
        answer.append(len(string)) # answer리스트에 string의 길이를 매번 추가해줌


    return min(answer) # 가장 작은 수를 출력

print(solution(s))