
# 작성자: red-Pen9uin
# Data structure: stack
# 17952_과제는 끝나지 않아!
# 수행 결과: 181396 KB / 1940 ms # 왜 이렇게 오래 걸리지?
"""
첫째 줄에 이번 학기가 몇 분인지를 나타내는 정수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

두번째 줄부터 N줄 동안은 학기가 시작하고 N분째에 주어진 과제의 정보가 아래의 두 경우 중 하나로 주어진다.

1 A T: 과제의 만점은 A점이고, 성애가 이 과제를 해결하는데 T분이 걸린다. A와 T는 모두 정수이다. (1 ≤ A ≤ 100, 1 ≤ T ≤ 1,000,000)
0: 해당 시점에는 과제가 주어지지 않았다.

성애가 받을 과제 점수를 출력한다.

"""
import sys

def get_score(assignment: list) ->None:
    assign_stack = list()
    time_stack = list()
    total_score = 0
    cnt = -1

    for assign_now in assignment:
        if assign_now[0] == 0:
            pass
        else:
            assign_stack.append(assign_now[1])
            time_stack.append(assign_now[2])
            cnt += 1

        if assign_stack:
            time_stack[cnt] -= 1

            if time_stack[cnt]==0:
                total_score += assign_stack[cnt]
                assign_stack.pop()
                time_stack.pop()
                cnt -= 1

    print(f"{total_score}")
    return


if __name__ == "__main__":
    t_min = int(sys.stdin.readline())
    assignment = list()

    for _ in range(t_min):
        assignment.append(list(map(int, sys.stdin.readline().split())))

    get_score(assignment)