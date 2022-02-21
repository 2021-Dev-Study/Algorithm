# 문자열 검색
# 1436_영화감독 숌

if __name__ == "__main__":
    N = int(input())
    name = 666
    cnt = 0

    while (True):
        # 만약 영화 이름에 '666'이 들어간다면 cnt에 1 증가
        if '666' in str(name):
            cnt += 1
        
        # 만약 cnt가 N과 같으면 영화 이름 출력하고 반복문 탈출
        if cnt == N:
            print(name)
            break
        
        # 영화 이름에서 1을 증가
        name += 1
