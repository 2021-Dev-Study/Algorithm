# 큐 (실버 3까지)
# 12034_김인천씨의 식료품가게

import sys
from collections import deque

if __name__ == "__main__":
    T = int(input())

    for k in range(1, T+1):
        N = int(sys.stdin.readline())
        queue = deque(list(map(int, sys.stdin.readline().split()))) # 입력받은 2N개의 정수를 덱으로

        lst = [] # 할인가를 저장할 빈 리스트
        while queue:
            num = queue.popleft() 
            for i in range (len(queue)):                
                if num*4//3 == queue[i]:
                    lst.append(num)
                    del queue[i]
                    break
            


        print(f'Case #{k}:', end='')
        for j in range(len(lst)):
            print(f' {lst[j]}', end='')
        print()    
        
        
                    
# 덱에서 제일 앞의 원소 일단 꺼내고 
# 그 원소에 해당하는 정상가가 덱 안에 존재하면 할인가는 lst에 저장하고 정상가는 덱에서 제거하기
# 이 과정을 덱이 빌 때까지 반복

# 9 9 12 12 12 15 16 20

# 9 | 9 12 12 12 15 16 20
# 덱의 제일 왼쪽 원소를 꺼낸뒤 뒤에 정상가가 있으면 덱에서 제거
# 할인가는 lst에 넣기
# (덱에서 제거 하는 이유는 정상가와 할인가를 구분하기 위해서)

# 9 12 12 15 16 20

# 9 | 12 12 15 16 20
# 덱의 제일 왼쪽 원소를 꺼낸 뒤 뒤에 정상가가 있으면 덱에서 제거
# 할인가는 lst에 넣기

# 12 15 16 20

# 12 | 15 16 20
# 덱의 제일 왼쪽 원소를 꺼낸 뒤 뒤에 정상가가 있으면 덱에서 제거
# 할인가는 lst에 넣기

# 15 20

# 15 | 20
# 덱의 제일 왼쪽 원소를 꺼낸 뒤 뒤에 정상가가 있으면 덱에서 제거
# 할인가는 lst에 넣기

 