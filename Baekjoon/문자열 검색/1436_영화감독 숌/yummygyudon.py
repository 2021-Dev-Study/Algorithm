import sys
N = int(sys.stdin.readline())
cnt = 0
title = 665 # while문의 첫 실행문을 +1로 하기 때문에
# cnt 가 1일 때는 무조건 666이 되어야하는 점
while cnt != N :
    title += 1
    if '666' in str(title) :
        cnt += 1
print(title)