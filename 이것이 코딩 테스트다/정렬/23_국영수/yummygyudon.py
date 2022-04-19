N = int(input())
ls = []
for _ in range(N) :
    name, k,e,m = input().split()
    ls.append([int(k),int(e),int(m),name])

ls.sort(key = lambda x : (-x[0],x[1],-x[2],x[3]))
for _,_,_,n in ls :
    print(n)