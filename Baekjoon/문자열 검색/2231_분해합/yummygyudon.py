import sys
N = int(sys.stdin.readline())
# 임의의 수와 그 수의 각 자리수와의 합이 N이 되는 가장 작은 경우를 출력
v = 0
for i in range(1, N+1) : # N이 1이상 1백만 이하이기 때문에 1이 들어올 수도 있다 => 1부터 하나씩
    s = i + sum(map(int,str(i))) # 문자열(str)로 변환하면 자연스럽게 각 자리에 인덱스가 부여되서 map 적용 가능
    # 1부터 시작하기 때문에 작은 수부터 나오기 때문에
    # 최초 동일 = 가장 작은 생성자
    if s == N :
        v = i
        print(i)
        break
if v == 0 : # for문 마다 i == N 의 if문을 실행하기엔 비효율....근데 48ms 차이밖에 안나네요..ㅋㅋㅋ
    print(0)