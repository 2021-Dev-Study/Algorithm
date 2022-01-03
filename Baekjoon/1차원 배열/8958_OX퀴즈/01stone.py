# OX퀴즈
'''
입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다. 
       각 테스트 케이스는 한 줄로 이루어져 있고, 
       길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
       문자열은 O와 X만으로 이루어져 있다.
출력 : 각 테스트 케이스마다 점수를 출력한다.
'''

cnt = int(input())

for _ in range(cnt):        # cnt 만큼 ox_list 만듦
    ox_list = list(input()) # 입력
    score = 0  
    score_sum = 0
    
    for ox in ox_list:
        if ox == 'O':       # O는 1점
            score += 1 
            score_sum += score
        else:               # x는 빵점
            score = 0
    print(score_sum)        # ox_list마다 합산 점수