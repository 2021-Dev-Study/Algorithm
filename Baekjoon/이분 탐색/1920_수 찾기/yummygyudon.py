s = set()
N = int(input())
nums = list(input().split())
for n in nums :
    s.add(n)
M = int(input())
ipt = list(input().split())
for i in range(M) :
    if ipt[i] in s :
        print(1)
    else :
        print(0)