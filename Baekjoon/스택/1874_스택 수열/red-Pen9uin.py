# 작성자: red-Pen9uin
# Data structure: stack
# 1874_스택 수열
# 수행 결과: 35504 KB / 180 ms
"""
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.

임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
이를 계산하는 프로그램을 작성하라.

첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다.
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
물론 같은 정수가 두 번 나오는 일은 없다.

입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
push연산은 +로,
pop 연산은 -로 표현하도록 한다.

불가능한 경우 NO를 출력한다.

"""
import sys


def get_numbers(num:list, t_size:int) ->None:
    stack = [0]
    dumped = set()
    i = 0
    cnt = 0
    now = 1
    result = ""
    while i < t_size :
        if num[i] in dumped:
            print("NO")
            return

        if stack[cnt] < num[i]:
            result = result + "+\n"
            stack.append(now)
            now += 1
            cnt += 1

        elif stack[cnt] == num[i]:
            result = result + "-\n"
            stack.pop()
            i += 1
            cnt -= 1

        else: # stack[cnt] > num[i]
            result = result + "-\n"
            dumped.add(stack.pop())
            # stack.pop()
            i += 1
            cnt -= 1


    print(f"{result}")
    return


if __name__ == "__main__":
    t_size = int(sys.stdin.readline())
    num = list()

    for _ in range(t_size):
        num.append(int(sys.stdin.readline()))
    
    get_numbers(num, t_size)