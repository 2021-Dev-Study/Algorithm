import sys
n = int(sys.stdin.readline().rstrip())
numbers = sorted(list(map(int,sys.stdin.readline().split())))
want = int(sys.stdin.readline())
start = 0
end = n-1
result = []
while start < end :
    s = numbers[start] + numbers[end]
    if s == want : # 원하는 값과 동일한 쌍을 찾으면
        # 정렬되어있기 때문에 start와 end 둘다 바깥쪽으로 이동할 필요없이 한칸씩 안으로 들어오면 됨.
        result.append([numbers[start], numbers[end]])
        start += 1
        end -= 1
    elif  s < want :
        # 두 쌍의 합이 작을 경우
        # 작은쪽인 왼쪽에서 큰쪽으로 한칸 이동해서 합이 더 커지게끔
        start += 1
    else :
        # 두 쌍의 합이 더 클 경우
        # 큰쪽인 오른쪽에서 작은쪽으로 한칸 이동해서 합이 작아지게끔
        end -= 1
print(len(result))
