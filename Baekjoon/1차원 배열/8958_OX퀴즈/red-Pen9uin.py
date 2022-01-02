# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 8958: OX퀴즈
"""
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
"""
import sys

def main():
    num = int(sys.stdin.readline())
    
    total = list()

    for i in range(0,num):
        temp = 0
        score = 0
        # result를 1차원 배열(string)으로 사용
        # 2차원 배열로 사용할까 했는데 필요하지 않아보여 수정
        # 수정 과정에서 다수의 런타임 에러 발생
        # 인덱스는 잘 잡도록 하자
        result = sys.stdin.readline()
        for j in range(0, len(result)):
            score += 1
            if result[j] == 'O':
                temp += score
            else:
                score = 0
        total.append(temp)
    
    for i in range(0,num):
        print(total[i])

if __name__ == "__main__":
    main()