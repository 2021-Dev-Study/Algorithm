# 평균은 넘겠지.
'''
입력 : 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
      둘째 줄부터 각 테스트 케이스마다 
      학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
      이어서 N명의 점수가 주어진다. 
      점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 
       반올림하여 소수점 셋째 자리까지 출력한다.
'''

num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]          # 평균~
    
    cnt = 0
    for i in scores[1:]:                     # 평균 넘은 점수 개수~
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100                # 평균 넘은 개수 퍼센트~
    print('%.3f' %per + '%')                 # 소수점 셋째자리~