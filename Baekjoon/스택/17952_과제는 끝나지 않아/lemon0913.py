# 스택 (실버 3까지)
# 17952_과제는 끝나지 않아!

import sys

if __name__ == "__main__":
    N = int(input())
    # 시간이 지남에 따라 남은 시간과 점수를 저장하는 리스트
    time = []
    score = []
    answer = []

    for i in range(N):
        x = list(map(int, sys.stdin.readline().split()))
        # 과제가 주어졌다면 시간과 점수를 각 리스트에 저장
        if x[0] == 1:
            score.append(x[1])
            time.append(x[2])
        # 과제가 주어지지 않았다면 패스
        else:
            pass
        
        # 들어온 과제가 있다면
        if time:
            # 다음 과제를 확인 하기 전에 시간이 지남에 따라 가장 최근 과제의 시간 감소시키기
            time[-1] -= 1
            # 만약 가장 최근 과제를 다 했다면
            if time[-1] == 0:
                time.pop()
                answer.append(score.pop())

    print(sum(answer))


