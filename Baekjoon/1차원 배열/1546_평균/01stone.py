# 평균
'''
입력 : 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 
       이 값은 1000보다 작거나 같다. 
       둘째 줄에 세준이의 현재 성적이 주어진다. 
       이 값은 100보다 작거나 같은 음이 아닌 정수이고, 
       적어도 하나의 값은 0보다 크다.
출력 : 첫째 줄에 새로운 평균을 출력한다. 
       실제 정답과 출력값의 절대오차 또는 상대오차가 
       10-2 이하이면 정답이다.
'''

sub = int(input())
sub_score = list(map(int, input().split()))
max_score = max(sub_score)

new_score = []
for score in sub_score:
    new_score.append(score/max_score*100) # 새로운 점수 = 원점수/최고점*100

print(sum(new_score)/sub) # 가짜점수 평균..사기꾼...