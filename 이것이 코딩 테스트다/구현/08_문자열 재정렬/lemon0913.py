if __name__ == "__main__":
    S = list(input())

    num = 0
    alp = []
    for s in S:
        if s.isalpha(): # s가 알파벳이면 alp배열에 추가
            alp.append(s)
        else: # s가 숫자면 합 구하기
            num += int(s)
    
    # alp배열을 오름차순으로 정렬한 뒤 숫자합을 추가하기
    alp.sort()
    alp.append(str(num)) # 숫자합을 str의 형태로 바꿔야 join 가능함
    print(''.join(alp))