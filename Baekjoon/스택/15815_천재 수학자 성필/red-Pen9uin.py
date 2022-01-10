# 작성자: red-Pen9uin
# Data structure: stack
# 15815_천재 수학자 성필
# 수행 결과:  KB /  ms
"""
우리 세계의 식을 문제의 식으로 바꾸는 방법을 간단히 설명하자면 이렇다.

우선 주어진 식을 연산자의 우선순위에 따라 괄호로 묶어준다.
그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다.
그다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 a+bc*가 된다.
마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

길이가 100이 넘지 않는 수식이 예제 입력과 같이 공백 없이 입력된다.
수식은 0부터 9까지의 숫자와 연산자 '+', '-', '*', '/' 로만 이루어져 있다.

또한, 수식의 계산 중간 과정의 모든 결과는 항상 2,147,483,647을 넘지 않는 정수이고 0으로 나누는 경우는 없습니다.
잘못된 수식이 입력되는 경우도 없습니다.

입력으로 주어진 성필의 수식의 답을 첫째 줄에 출력한다.
"""
import sys

""" 풀이 진행중 """
def translate_cal(word:str) -> int:
    numbers = list()
    oper = list()

    for i in range(1, index+1):
        temp = int(word[index - i])
        if word[index + i] == '+':
            ans += temp
        elif word[index + i] == '-':
            ans -= temp
        elif word[index + i] == '*':
            ans *= temp
        elif word[index + i] == '/':
            ans //= temp
    print(ans)


def calcutate_ans(cal: list)-> int:
    index = len(word)//2
    ans = int(word[index])
    # print(index)

    for i in range(1, index+1):
        temp = int(word[index - i])
        if word[index + i] == '+':
            ans += temp
        elif word[index + i] == '-':
            ans -= temp
        elif word[index + i] == '*':
            ans *= temp
        elif word[index + i] == '/':
            ans //= temp
    print(ans)


if __name__ == "__main__":
    word = sys.stdin.readline().rstrip('\n')
    translate_cal(word)
    