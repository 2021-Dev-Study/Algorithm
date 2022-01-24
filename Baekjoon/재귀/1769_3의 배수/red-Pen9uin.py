# 작성자: red-Pen9uin
# level 10: Recursion
# 1769_3의 배수
# 수행 결과: 32820 KB / 232 ms
"""
소위 "다른 문제로 바꾸어 풀기"라는 이 방법은, 아래와 같은 과정으로 이루어진다.

풀고자 하는 문제를 다른 문제로 변환한다.
변환된 문제의 답을 구한다.
구한 답을 원래 문제의 답으로 삼는다.

이를 보다 쉽게 이해하기 위해서, 다음의 초등학교 수학 수준의 예를 들어 보자.

문제 1. "양의 정수 X는 3의 배수인가?"
문제 2. "Y는 3의 배수인가?"

문제 1을 풀고 싶으면 문제 2로 변환을 해서 문제 2의 답을 문제 1의 답으로 삼으면 된다.



당신이 알고 있는 3의 배수는 한 자리 수밖에 없다고 가정하자.

즉, 문제 변환의 과정을 여러 번 거치다 보면 Y가 한 자리 수가 되는 순간이 있게 되는데,
그렇게 될 때까지 문제 변환을 반복한다는 뜻이다.

변환 후의 Y가 3, 6, 9 중 하나이면 원래의 수 X는 3의 배수이고,
Y가 1, 2, 4, 5, 7, 8 중 하나이면 원래의 수 X는 3의 배수가 아니다.

큰 수 X가 주어졌을 때,
앞에서 설명한 문제 변환의 과정을 몇 번 거쳐야 Y가 한 자리 수가 되어,
X가 3의 배수인지 아닌지를 알 수 있게 될지를 구하는 프로그램을 작성하시오.

"""
# 재귀로 푼다는 건 계속 각 자릿수를 더한 값을 이용해 호출한다는 뜻

import sys


def is_3_multi(num: str, cnt: int):
    
    if len(num) > 1:
        count = cnt+1
        sum = 0
        for i in num:
            sum += int(i)
        ret = is_3_multi(str(sum), count)

        return ret
    else:
        print(cnt)
        return num


if __name__ == "__main__":
    num = sys.stdin.readline().rstrip('\n')
    ret = is_3_multi(num, 0)
    # cnt = 0

    # while True:
    #     if len(num) > 1:
    #         cnt = cnt+1
    #         sum = 0
    #         for i in num:
    #             sum += int(i)
    #         num = sum
    #         continue
    #     else:
    #         print(cnt)
    #         break

    is_multi = [3, 6, 9]
    if int(ret) in is_multi:
    # if num in is_multi:
        print("YES")
    else:
        print("NO")