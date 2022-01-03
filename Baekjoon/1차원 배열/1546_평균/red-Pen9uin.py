# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 1546: 평균
"""
세준이는 기말고사를 망쳤다.
세준이는 점수를 조작해서 집에 가져가기로 했다.
일단 세준이는 자기 점수 중에 최댓값을 골랐다.
이 값을 M이라고 한다.
그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

세준이의 성적을 위의 방법대로 새로 계산했을 때,
새로운 평균을 구하는 프로그램을 작성하시오.

실제 정답과 출력값의 절대오차 또는 상대오차가 10^(-2) 이하이면 정답이다.
python은 자료형을 자동으로 잡아주기 때문에 신경쓸 것이 별로 없었던 것 같다.
"""
import sys

def main():
    num = int(sys.stdin.readline())
    score = list(map(int, sys.stdin.readline().split()))
    # 최대, 최소를 구하는 것이 중점인 문제가 아니므로 max()를 이용함
    max_score = max(score)
    new_mean = 0

    for i in range(0,num):
        new_mean += score[i] / max_score * 100

    new_mean /= num

    print(new_mean)

if __name__ == "__main__":
    main()