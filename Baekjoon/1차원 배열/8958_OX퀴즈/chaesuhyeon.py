n = int(input()) # 테스트 개수 입력

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum = 0 
    for ox in ox_list:
        if ox == 'O':
            score += 1 # 'O'가 연속했을 때 누적됨
            sum += score
        else:
            score = 0 # "X"이면 score 초기화 
    print(sum)