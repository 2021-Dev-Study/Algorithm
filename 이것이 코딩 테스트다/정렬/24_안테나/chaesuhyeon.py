import sys
n = int(sys.stdin.readline().rstrip())
house = list(map(int,sys.stdin.readline().rstrip().split()))
house.sort()

if n % 2 == 1:
    print(house[n//2])
else:
    print(house[n//2 -1])
