import sys
t = int(sys.stdin.readline().rstrip())
# 할인된 가격 또한 정수라고 했기때문에 3으로 나눈 나머지가 0인 값
#.....424ms....
for test in range(1, t+1) :
    dis = []
    n = int(sys.stdin.readline().rstrip())
    p = sys.stdin.readline().rstrip().split()
    print(f"Case #{test}:",end='')
    for i in range(n) :
        max = int(p[-1])
        ptr = 0
        for num in p :
            if float(num) == int(max*0.75) :
                dis.append(num)
                p.pop(ptr)
                p.pop(-1)
                break
            ptr+=1
    for i in range(len(dis)-1,-1,-1) :
        print(f" {dis[i]}",end='')
    print()

#.....404ms....
for test in range(1, t+1) :
    dis = []
    n = int(sys.stdin.readline().rstrip())
    p = sys.stdin.readline().rstrip().split()
    print(f"Case #{test}:",end='')
    while len(dis) < n :
        max = int(p[-1])
        ptr = 0
        for num in p :
            if float(num) == int(max*0.75) :
                dis.append(num)
                p.pop(ptr)
                p.pop(-1)
                break
            ptr+=1
    while len(dis) != 0:
        print(f" {dis.pop()}",end='')
    print()

