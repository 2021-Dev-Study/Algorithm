def solution(new_id):
    answer = ''
    # 소문자화
    string = new_id.lower()
    # 소문자, 숫자, 빼기, 밋줄, 마침표
    for ch in string:
        if ch in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
            answer += ch
    # 복수의 .을 하나의 .으로
    while ".." in answer:
        answer =answer.replace("..", ".")
    
    # 첫글자 . 없애기
    if answer[0] == ".":
        answer = answer[1:]
    
    # 끝글자 . 없애기
    if len(answer):
        if answer[-1] == ".":
            answer = answer[:-1]
    
    # 빈칸 -> a
    if not len(answer):
        answer += "a"
    
    # 16 이상 -> 15
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 2 이하 -> 3
    while len(answer) <= 2:
        answer += answer[-1] 
    
    return answer