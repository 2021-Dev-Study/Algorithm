# 정렬
# 10825_국영수

import sys
if __name__ == "__main__":
    N = int(input())
    # 각 학생의 정보 입력받기
    # 각 학생의 국, 영, 수 성적은 정수로 변환해서 저장
    students = []
    for i in range(N):
        students.append(list(sys.stdin.readline().split()))
        students[i][1], students[i][2], students[i][3] = int(students[i][1]), int(students[i][2]), int(students[i][3])
    
    # 국어 점수를 내림차순 -> 영어 점수를 오름차순 -> 수학점수를 내림차순 -> 이름을 오름차순으로 정렬
    students.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

    # 학생 이름만 출력
    for i in students:
        print(i[0])