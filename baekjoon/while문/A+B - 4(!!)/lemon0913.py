import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)


#EOF에 대해 알아보자.
#입력이 있을 때는 계속 입력을 받아와 원하는 연산을 하고, EOF가 발생하면 반복문을 빠져나온다
#sys.stdin.readline()을 사용하면 자동으로 EOF처리가 되나, input()을 이용할 경우 try와 except EOFError 예외 처리가 필요하다
#input()함수 사용에 따른 예제는 다음과 같다.

# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except EOFError:
#         break
