C = int(input()) # 테스트 개수 
a = []

for i in range(C):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0] # index 1부터는 학생의 점수 / index 0 은 학생의 수
    student = 0
    for score in a[1:]:
        if score > avg :
            student +=1 # 평균을 넘는 학생의 수를 구함 
    rate = student / a[0] * 100
    print(f'{rate:.3f}%') # .3f  소수점 3자리까지 표시