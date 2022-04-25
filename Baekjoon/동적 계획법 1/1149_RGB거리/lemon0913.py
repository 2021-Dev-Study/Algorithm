import sys
if __name__ == "__main__":
    N = int(input())

    home = [0] * N
    for i in range(N):
        home[i] = list(map(int, sys.stdin.readline().split()))
    
    for i in range(1, N):
        home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
        home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1]
        home[i][2] = min(home[i-1][1], home[i-1][0]) + home[i][2]
    
    print(min(home[N-1]))

# 26 40 83
# 49 60 57
# 13 89 99


