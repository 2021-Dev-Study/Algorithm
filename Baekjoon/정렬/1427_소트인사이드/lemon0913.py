# 정렬 (단계별)
# 1427_소트인사이드

if __name__ == "__main__":
    # N을 문자열로 입력받은 뒤 int형읋 바꿔 lst에 저장
    N = input()
    lst = []
    for i in range(len(N)):
        lst.append(int(N[i]))
    
    # 내림차순으로 정렬해서 출력
    lst.sort(reverse=True)

    for i in lst:
        print(i, end='')