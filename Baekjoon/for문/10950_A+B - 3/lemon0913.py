T = int(input())
A = [0]*T
B = [0]*T


for i in range(0, T):
    A[i], B[i] = map(int, input().split())

for i in range(0, T):
    print(A[i]+B[i])

#A = list(), B = list() 한 뒤에 A[i], B[i] = map(int, input().split())을 하면 에러가 뜬다
#빈 리스트인데 0번 인덱스가 어디있니? 하는 것이다...
#대신에 A = [0]*T, B = [0]*T을 써서 0값이 들어가 있는 T개의 방을 잡아놓자!

#T개 만큼의 A,B를 한번에 입력받은 뒤, 출력도 한번에 보여주는건가 아니면 A,B를 입력받을 때마다 출력하는 건가..??
