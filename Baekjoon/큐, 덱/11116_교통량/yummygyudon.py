# 왼쪽에서 왔다면 왼쪽박스 쪽에 더 작은 [t, t+500]짝과
# 오른쪽 박스 측정값 리스트에 무조건 1000씩 더 큰 [t+1000, (t+500)+1000]짝이 있어야함
# 만약 왼쪽에 있는 짝에서 -1000씩 뺀 값들의 짝이 오른쪽에 있으면  오른쪽에서 온 차임.
# 한번에 차 한대만 지날 수 있기 때문에 1000씩 차이나는 값은 같은 차일 수 밖에 없음
# 왼쪽만 순서대로 보면서 오른쪽 측정값들 중 t보다 1500 큰 값이 있는지 확인하면 됨

import sys
case = int(sys.stdin.readline().rstrip())
for c in range(1,case+1) :
    m = int(sys.stdin.readline().rstrip()) # 이 m을 사용할 곳이 없군요... 측정값 개수를 쓸데가 어디있을까요..
    lm = list(map(int,sys.stdin.readline().rstrip().split()))
    rm = list(map(int,sys.stdin.readline().rstrip().split()))
    cnt = 0
    left = 0
    while len(lm) > 0 :
        i = lm.pop(-1)
        for n in rm :
            if (i+1500) == n :
                cnt += 1
    print(cnt)

