def solution(s):
    if len(s)==1:
        return 1
    answer = [] # 1개 단위, 2개 단위, ...로 압축했을 때 길이를 담는 배열
    for i in range(1, len(s)//2+1): # 1~원본 문자열의 절반 길이로 압축시킨다
        result = ""
        x = s
        while x: 
            tmp = x[:i] # 압축기준
            cnt = 0
            while x[:i] == tmp: 
                cnt += 1
                x=x[i:]
            if cnt > 1:
                result += str(cnt)
            result += str(tmp)
        answer.append(len(result))
        
        
    return min(answer)