import sys

input = sys.stdin.readline
N, wanna = map(int, input().split())
trees = list(map(int, input().split()))
end = max(trees)
start = 1

while start <= end:
    s = 0
    mid = (end + start) // 2
    for len in trees:
        if len >= mid:
            s += (len - mid)

    if s >= wanna:
        # end를 출력하기 때문에 반복문 종료를 위해서
        # wanna 값과 일치했을 경우엔 start를 mid+1 로 해주면 무조건 end를 넘어가서
        # 반복문을 종료시키고 end를 출력시킬 수 있다.
        start = mid + 1
    else:
        end = mid - 1
print(end)