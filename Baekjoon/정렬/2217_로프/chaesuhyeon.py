# max_weight에서 값 * 로프의 개수(N)
import sys
N = int(sys.stdin.readline().rstrip())
rope = [0] * N 
for i in range(N):
    rope[i] = int(sys.stdin.readline().rstrip())

rope.sort(reverse=True) # 큰 값부터 계산하기 위해 

mw = 0 # max_weight
for i in range(N):
    w = rope[i] * (i+1) # rope는 한개부터 (모든 로프를 다 이용할 필요는 없으므로)
    if w > mw : # w 가 mw보다 크면 최댓값이므로 
        mw = w # w값을 mw에 대입
print(mw) # 최댓값 출력




