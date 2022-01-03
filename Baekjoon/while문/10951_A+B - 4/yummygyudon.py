# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# 예외처리구문 활용 문제 (참고)
# 입력값이 있을 동안만(없을 때까지) -> 더 이상 case 없으면 오류 -> except문으로 나오기

# 계산 과정은 for문 문제들 중의 A+B 문제들과 유사
import sys
while True:
    try :
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except :
        break

# 이 방법도 가능 _예외 처리 구문을 가장 바깥으로 while을 안으로 넣고 exit()으로 끝내기
try :
    while True :
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
except :
    exit()