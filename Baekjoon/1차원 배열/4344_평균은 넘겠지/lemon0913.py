# level 5 - 1차원 배열
# 4344번 평균은 넘겠지


# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.



#케이스별로 평균을 넘는 학생들의 비율 출력하는 함수 정의
def avg_per(str):
    
    #일단 케이스별로 평균 구하기
    sum = 0
    avg = 0
    for i in range(1, len(str)):
        sum = sum + str[i]
    avg = sum / str[0]

    #각 케이스마다 평균을 넘는 학생의 수 구하기
    count = 0
    for i in range(1, len(str)):
        if str[i] > avg:
            count += 1
    
    #각 케이스마다 평균을 넘는 학생들의 비율 구하기
    per = (count / str[0])*100
    #반올림해서 소수점 셋째자리까지 출력하기
    per = round(per, 3)

    print(f'{per:.3f}%')





if __name__ == "__main__":
    #테스트 케이스 입력받기
    C = int(input())
    ary = [0] * C
    for i in range(C) :
        ary[i] = list(map(int, input().split()))

    for i in range(C):
        avg_per(ary[i])





#반올림해서 소수점 셋째자리까리 출력하기위해 서식지정자를 활용함
#rate:.3f --> rate의 소수점 셋째자리까리 출력하기