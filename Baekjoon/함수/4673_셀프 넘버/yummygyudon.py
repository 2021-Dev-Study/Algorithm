def d(n) : # 무한 수열만들기 위한 셀프넘버 함수
    if n < 10 :
        return n+n
    else :
        num = [int(s) for s in str(n)]
        return n+sum(num)

s = set([d(n) for n in range(1,10001)]) # 생성자가 한개보다 많을 경우를 대비해서 set 자료형 사용
for i in range(1,10001) :
    if i not in s : # 해당 수열에 없을 경우에만 출력
        print(i)

