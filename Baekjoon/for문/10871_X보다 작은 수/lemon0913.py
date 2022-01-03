N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(0, N):
    if A[i] < X:
        print(A[i], end=' ')

#수열A를 이루는 정수 N개를 입력받는 방법은 list()합수를 사용하면 됨.
#A=list([1,2,3])이나 A=list({1,2,3}) 이런식으로 사용가능하다. 이를 염두해 응용해보자
