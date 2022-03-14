if __name__ == "__main__":
    N = int(input())
    tour = list(map(int, input().split()))
    tour.sort()
    
    cnt = 0
    group = 0
    for i in tour:
        if i > group:
            group += 1
        if i == group:
            cnt += 1
            group = 0
    print(cnt)