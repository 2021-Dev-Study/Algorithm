# 작성자: red-Pen9uin
# level 6: function
# 1330: 두 수 비교하기
"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면,
그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.

N이 주어졌을 때, 1보다 크거나 같고,
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

"""
import sys

def is_arithmetic(num: int) -> int:
    count = 0
    check = False
    if num<100:
        count = num
    else:
        # 100 이전의 모든 숫자는 자릿수가 1개 혹은 2개이므로,
        # 모두 등차수열을 이룬다고 할 수 있다.
        count += 99

        for i in range(100, num+1):
            temp = i
            while temp//100 > 0:
                a = temp%10
                b = (temp//10) %10
                c = (temp//100) %10
                if (a-b) == (b-c) :
                    check = True
                else:
                    check = False
                    # 한번이라도 깨지면 루프를 끝낸다
                    break
                temp //= 10
            if check:
                count += 1

    return count

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    print(is_arithmetic(num))