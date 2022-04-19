def solution(food_time : list, k : int) :
    from collections import deque
    q = deque()
    idx = 1
    for f in food_time :
        q.append([idx, f])
        idx += 1
    cnt = 0
    while cnt < k :
        print()
        if not q :
            print(f"장애 발생 전에 벌써 다먹음")
            return -1
        print(f"현재 돌림판 : {q}")
        id, times = q.popleft()
        print(f"<{cnt}초 ~ {cnt+1}초>")
        if times == 0:
            continue
        else :
            cnt += 1
            print(f"이번에 먹을 음식은 {id}번")
            q.append([id,times-1])
    print()
    print(f"5초 네트워크 장애 발생 시  돌림판 : {q}")
    return q[0][0]


if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5

    print(solution(food_times, k))