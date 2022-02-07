import sys
N = int(sys.stdin.readline())
num=[]
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    num.append([y, x]) # y를 기준으로 정렬해야 하므로 순서 바꿔서 append 

num.sort() 

for i in range(N):
    print(num[i][1], num[i][0]) # x y 순서대로 출력을 해야하므로 [1] , [0] 으로 출력 


########## lamda를 이용한 풀이 참고 ##########
import sys
N = int(sys.stdin.readline())
num=[]
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    num.append([x, y])

num.sort(key=lambda z: (z[1], z[0])) 
# lamda를 사용해서 정렬기준을 정해주는데 y축 먼저 정렬하고나서 x축 정렬함 

for i in range(N):
    print(num[i][0], num[i][1])