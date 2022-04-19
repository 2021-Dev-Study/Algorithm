S = list(input())
n = len(S)
v1 = sum(map(int,S[:(n//2)]))
v2 = sum(map(int,S[n//2:]))
if v1 == v2 :
    print('LUCKY')
else :
    print('READY')