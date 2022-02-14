import sys
n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline().rstrip()) 
cnt = 0
left, right = 0, n-1

while left < right: # 왼쪽 인덱스가 오른쪽 인덱스보다 작을 경우에만 반복수행
    num = arr[left] + arr[right]
    if num == x: # x(비교값)면 cnt + 1 해주고,  작은 숫자부터 증가시켜 비교 
        cnt += 1
        left +=1
    elif num < x: # 비교값 x보다 더한값 num이 작다면 작은 숫자부터 증가시킴
        left += 1
    else: # 비교값 x보다 더한값num이 크다면 큰숫자 인덱스를 하나씩 감소시켜  비교
        right -= 1
print(cnt)
