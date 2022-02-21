#브루트포스
# 2231_분해합

# 이것도 부르트포스임...왜..??
import sys
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, sys.stdin.readline().split())))

    # 달리 방법이 없음..그냥 자기보다 크고 무거운 사람이 몇 명인지 새서 자기 등수를 정해야 됨
    result = []
    for i in range(N):
        rank = 1
        for j in range(N): # i번째 사람보다 크고 무거운 사람이 있으면 i의 rank를 증가시키기
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                rank += 1
        print(rank, end=' ') # i의 rank 출력