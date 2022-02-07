# 정렬 (단계별)
# 10814_나이순 정렬

# 파이썬은 stable sort -> 입력 받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지한다
import sys
if __name__ == "__main__":
    N = int(input())
    lst = [0] * N
    for i in range(N):
        lst[i] = list(sys.stdin.readline().split())
        lst[i][0] = int(lst[i][0])  # 입력받은 나이를 str에서 int로 변경
 
    
    # 나이값으로만 정렬을 한다 -> 파이썬은 stable sort라서 나이값이 같은 경우에 입력 받은 순서를 그대로 유지한다
    lst.sort(key = lambda x: x[0])

    for i in range(N):
       print(lst[i][0], lst[i][1])
