def hanoi(num, start, end, sub ) :
    if num == 1: # 원반의 개수가 1개 남으면 3번째 기둥(목표)으로 옮기고 리턴 
        print(start, end) # 2
        return
    hanoi(num-1, start, sub, end) # 1
    print(start, end) # 2
    hanoi(num-1, sub, end, start) # 3

num = int(input())
print(2**num -1) # 횟수 출력 
hanoi(num, 1, 3, 2) # num개의 원반을 1번 기둥에서 3번 기둥으로 옮기는데 2번 기둥을 보조로 사용 

# def hanoi(num, start, end, sub ) --> num개의 원반을 start기둥에서 end기둥으로 옮기는데 sub기둥을 보조로  사용하겠다는 코드
# 원반이 두개 이상이면 맨 밑 원반(제일 큰 원반)을 제외하고 (원반개수 -1)개의 원반을 보조 기둥으로 옮김 #1번 코드 
# 시작 기둥에 맨 밑 원반이 남았으므로 이 원반을 목표 기둥으로 옮겨야 함 #2번 코드 
# 목표 기둥에 제일 큰 원반이 놓이게 되면 이제 목표 기둥에 옮겨야할 원반의 개수는 (처음 원반의 개수 -1)개임 . 
# 시작 기둥은 비어있고 보조 기둥에 나머지 원반들이 있으므로 보조 기둥을 시작기둥으로, 시작 기둥을 보조기둥으로 바꿈 #3번 코드 