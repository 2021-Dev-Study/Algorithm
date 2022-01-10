# 스택 (실버 3까지)
# 17413_단어 뒤집기 2


if __name__ == "__main__":
    S = input()
    tmp = [] 
    ans = []
    flag = True #괄호 안이면 flag를 False로 바꿈

    # 괄호 사이는 그대로 두어야 함 -> 열린 괄호를 만나면 닫힌 괄호를 만날 때 까지 냅두기
    # 괄호 밖의 숫자, 영어는 순서 뒤집기
    # 공백은 냅두기
    for ch in S:
        if ch == "<":
            tmp.append(ch)
            flag = False
        elif ch == ">":
            tmp.append(ch)
            flag = True
        elif i == " ":


