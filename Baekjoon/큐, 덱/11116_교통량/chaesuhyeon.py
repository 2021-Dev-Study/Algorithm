import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    cnt = 0
    m = int(sys.stdin.readline().rstrip())
    lm = deque(map(int, sys.stdin.readline().rstrip().split())) # 왼쪽 
    rm = deque(map(int, sys.stdin.readline().rstrip().split())) # 오른쪽

    while lm: # 왼쪽 데이터가 존재하는 동안
        p = lm.popleft() # 맨 왼쪽 데이터 pop
        
        if p +500 in lm: # pop한 데이터에서 + 500인 데이터 있으면 오른쪽 데이터에서 +1000한 데이터도 있는지 검사   
            if p + 1000 in rm:
                cnt += 1  # 오른쪽 데이터에서 +1000인 데이터까지 있으면 cnt +=1 해줌 
                
        elif p + 1000 in rm: # 앞에 pop한 숫자와 짝일 경우 ex )앞에서 17이였는데 517일 경우  +500인 데이터는 없기 때문에 바로 오른쪽 검사 
            continue # 카운트 해줄필요 없으므로 continue써서 다시 반복 
        
    print(cnt) # 테스트 케이스마다 개수 출력 
