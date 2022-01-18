import sys
n, k = map(int,sys.stdin.readline().rstrip().split())
# 인덱스가 지워지면 다음값은 자동으로 해당 인덱스가 그대로 다음 값의 인덱스가 되기 때문에
# 인덱스는 수정할 필요 없고
# 만약 한 사이클을 돌고 돌아올 때는 '기념품'문제 처럼 나머지 값을 사용하면 됨.
que = [int(i) for i in range(1,n+1)]
result = []
idx = 0
print("<",end='')
for i in range(n) :
    idx +=  k-1 # 번째는 실제 해당 번째 인덱스보다 1 크기 때문에
    if idx >= len(que) :
        idx = idx%len(que) # 1번째부터 n번째 => 인덱스에선 0번째부터 n-1번째 라고 생각하면 편함
        # 한 사이클이 넘어갈 때 나머지로 que 머리에서부터 셈
    result.append(que.pop(idx))
    print(f"{result[i]}", end='')
    if len(que) == 0:
        print(">")
    else:
        print(", ", end='')

# 얘가 런타임 더 긺
que = [int(i) for i in range(1,n+1)]
idx = 0
print("<",end='')
for _ in range(n) :
    idx +=  k-1 # 번째는 실제 해당 번째 인덱스보다 1 크기 때문에
    if idx >= len(que) :
        idx = idx%len(que) # 1번째부터 n번째 => 인덱스에선 0번째부터 n-1번째 라고 생각하면 편함
        # 한 사이클이 넘어갈 때 나머지로 que 머리에서부터 셈
    print(f"{que.pop(idx)}", end='')
    if len(que) == 0:
        print(">")
    else:
        print(", ", end='')


# 예제는 통과
# front = rear = 0
# no = capacity = n
# que = [int(i) for i in range(1,n+1)]
# ls = [None]*capacity
# ptr = 0
# print("<",end='')
# while no != 0:
#     idx = (front+3)%no -1
#     print(f"{que.pop(idx)}", end='')
#     if len(que) == 0 :
#         print(">")
#     else:
#         print(", ", end='')
#     ptr += 1
#     if idx < 0:
#         front = 0
#     else:
#         front = idx
#     no -= 1

