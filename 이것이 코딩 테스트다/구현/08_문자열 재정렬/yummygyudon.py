S = list(input())
S.sort()

num = ['0','1','2','3','4','5','6','7','8','9']
n = 0

for s in S:
    if s in num :
        n+= int(s)
    else :
        print(s, end='')
print(n)
