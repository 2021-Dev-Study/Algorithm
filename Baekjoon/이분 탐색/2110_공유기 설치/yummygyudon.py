import sys
input = sys.stdin.readline

N, C = map(int, input().split())
h = []
for _ in range(N) :
    h.append(int(input()))
h.sort()

start = 1
end = h[N-1]
ans = 0
while start <= end :
    dis = (start + end) // 2 # 처음에는 중간값을 거리로
    '''
    공유기 개수가 부족하면 end를 줄여서 거리 줄여보기
    공유기 개수가 같으면 (start+1)로 end를 넘어가게 하기
    공유기 개수가 넘으면 충분하기 때문에 거리 늘려보기
    '''
    st = h[0]
    cnt = 1 # 첫집에 무조건 공유기 한 개 설치

    for i in range(1, N) :
        if h[i] >= st+dis : # 가장 최근에 설치한 집으로부터 기준 거리 떨어져 있거나 더 멀리 떨어져 잇는 경우 OK
            cnt +=1
            st = h[i] # 최근 설치 집 갱신

    if cnt >= C :
        ans = dis
        '''
        처음에는 cnt가 많아서 넘어갔는데 end보다 작거나 같아서 통과가 됐는데
        그다음엔 cnt가 기준보다 작게 되버려서
        아래 else 문에 해당되서 끝나는 경우 잘못된 dis 갱신을 할 수도 있기 떄문에
        print( dis -1 )을 하면 안된다
        < 기준 : 최대 거리 : 공유기 갯수만큼 설치 가능한 최대 거리 >
        '''
        start = dis+1
    else :
        end = dis-1
#print(dis-1)
print(ans)