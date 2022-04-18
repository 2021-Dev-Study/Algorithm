import sys
if __name__ == "__main__":
    K, N = map(int, input().split())
    lines = [0] * K
    for i in range(K):
        lines[i] = int(sys.stdin.readline().replace('\n', ''))
    

    start = 1  # start를 0으로 두니 zerodivisionError 발생
    end = max(lines)

    result = 0
    while start <= end:
        mid = (start+end)//2  # 자르는 단위 정하기

        # 잘린 길이가 몇개 나오는지 구하기
        cnt = 0
        for x in lines:
            cnt += x//mid
        
        
        if cnt < N: # N개보다 적게 잘렸다면 자르는 단위를 줄이기
            end = mid - 1
        else: # N개보다 많이 잘렸다면 자르는 단위를 늘려서 최대로 자를 수 있는 단위로 조정하기
            start = mid + 1
            result = mid # 일단 정답이 될 수 있는 값이므로 result에 저장
    
    print(result)



