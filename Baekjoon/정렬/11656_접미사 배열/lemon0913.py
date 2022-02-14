# 정렬
# 11656_접미사 배열

if __name__ == "__main__":
    S = input()

    # S의 접미사 구하기
    # S의 가장 앞 단어를 제거한 문자열(=접미사)를 lst에 저장
    lst = []
    for i in range(len(S)):
        x = S[i:]
        lst.append(x)

    # lst를 오름차순으로 정렬해 출력하기
    lst.sort()
    for i in lst:
        print(i)