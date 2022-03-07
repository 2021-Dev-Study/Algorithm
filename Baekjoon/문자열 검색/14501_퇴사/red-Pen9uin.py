# 작성자: red-Pen9uin
# Classification: string search
# 14501_퇴사
# 수행 결과:  KB /  ms
"""
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며,
1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

"""
import sys

def solve(num, case_time, case_pay):
    most_pay = [0]*25

    for i in range(num-1, -1, -1): # 역순으로 진행
        if case_time[i]+i <= num: # 날짜를 초과하지 않을 경우.
            #가장 큰 값을 저장
            most_pay[i] = max(case_pay[i] + most_pay[i + case_time[i]], most_pay[i+1])
        else: # 날짜 초과
            most_pay[i] = most_pay[i+1]
    print(most_pay[0])

if __name__ == "__main__":
    num = int(sys.stdin.readline())
    case_time, case_pay = [0]*num, [0]*num

    for i in range(num):
        case_time[i], case_pay[i] = map(int, sys.stdin.readline().split())

    solve(num, case_time, case_pay)