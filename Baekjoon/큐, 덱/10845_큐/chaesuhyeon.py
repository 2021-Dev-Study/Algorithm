
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

## 처음 푼 풀이가 시간초과가 났는데 어디가 틀린지 몰라서 아이디어만 찾았음.
## 리스트의 요소를 빼는 것이 아닌, 그냥 가리키는 index만 +1씩 해주면 시간복잡도가 훨 줄음

import sys

N = int(sys.stdin.readline())
queue = []
idx = 0
for n in range(N):
    menu = sys.stdin.readline().split()

    if menu[0] == "push":
        queue.append(menu[1])
        
    
    elif menu[0] == "pop":
        if len(queue)-idx == 0:
            print(-1)
        else:
            print(queue[idx])
            idx += 1
    
    elif menu[0] == "size":
        print(len(queue)-idx)
    
    elif menu[0] == "empty":
        if len(queue)-idx == 0:
            print(1)
        else:
            print(0)
    
    elif menu[0] == "front":
        if len(queue)-idx == 0:
            print(-1)
        else:
            print(queue[idx])
    elif menu[0] == "back":
        if len(queue)-idx == 0:
            print(-1)
        else:
            print(queue[-1]) 