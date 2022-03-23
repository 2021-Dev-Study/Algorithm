# 0 : 홈 패인 부분 / 1 : 돌기 부분
# 자물쇠는 NxN 정사각
# 열쇠는 MxM 정사각
# 풀 수 있으면 true / 없으면 false

# key를 90도 180도 270도 돌린 경우까지 모두 완탐
# lock 요소 + key 요소의 값이 1일 때 들어 맞는다는 의미 하나라도 2가 나오게 되면

# lock 은 돌릴 수 없음.
def key_rotate(arr) :
    n = len(arr)
    m = len(arr[0])
    result = [[0]*m for _ in range(n)] # key 돌린 값 저장할 백지 이차원배열
    for i in range(n) :
        for k in range(m) :
            # 정사각 키이기때문에 n에서 빼든 m에서 빼든 상관 X
            result[k][n-i-1] = arr[i][k]
    return result


def key_check(lock_y, lock_x,new_lock:list, key:list) :
    m = len(key)
    for i in range(m-lock_y) : #
        for k in range(m-lock_x) : #
            if (new_lock[lock_y][lock_x] + key[i][k]) != 1 :
                return False
    return True


def solution(key, lock) :
    N, M = len(lock[0]), len(key[0])
    for _ in range(4) :
        new_lock = lock.copy()
        key = key_rotate(key)
        # print(key)
        # print(new_lock)
        # print()
        for i in range(N) :
            for k in range(N) :
                if key_check(i, k, new_lock, key) :
                    return True
    return False








if __name__ == "__main__" :
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key, lock))
    # if solution(key, lock) :
    #     print("true")
    # else :
    #     print("false")