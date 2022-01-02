# 문자열 반복

trial = int(input())
for i in range(trial):
    num, word = input().split()
    result = ''
    for i in word:
        result += int(num)*i  # num만큼 word 문자열로..
    print(result)             # 출력