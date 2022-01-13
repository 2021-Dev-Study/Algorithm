# 작성자: red-Pen9uin
# level 5: 1 Dimensional Array
# 4344: 평균은 넘겠지
"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
당신은 그들에게 슬픈 진실을 알려줘야 한다.

각 케이스마다 한 줄씩
평균을 넘는 학생들의 비율을
반올림하여 소수점 셋째 자리까지 출력한다.
"""
# 재채점을 제일 많이 받은 문제지만 왜 그랬는지 원인분석이 애매하다.

import sys

def main():
    case = int(sys.stdin.readline())
    # above_mean = list()

    for i in range(0, case):
        cnt = 0

        input = list(map(int, sys.stdin.readline().split()))
        # input[0] = no of students
        # input[1]~[end] = score of students

        # 평균
        # index slicing을 통한 방법을 검색을 통해 찾음
        avg = sum(input[1:]) / input[0]

        for j in range(0, input[0]):
            if input[j+1]>avg :
                cnt += 1

    #     above_mean.append(cnt/input[0]*100)
    # for i in range(0,case):
    #     print("%0.3f" % above_mean[i] + "%")
    
    # 각 케이스마다 한 줄씩 출력할 것...
        above_mean = cnt / input[0] * 100
        print("%0.3f" % above_mean + "%")
        # print( f'{above_mean:.3f}%' )

if __name__ == "__main__":
    main()