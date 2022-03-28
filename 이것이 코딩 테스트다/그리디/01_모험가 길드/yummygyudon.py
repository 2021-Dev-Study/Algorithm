N = int(input())
adventurer = list(map(int, input().split()))
adventurer.sort(reverse=True)
# print(adventurer)

cnt = adventurer[0]
group = 1 # 공포도 큰 모험가부터 1팀으로 결성 시작
for x in adventurer[1:] :
    cnt -= 1
    if cnt == 0 : # 한팀 마감
        group+=1 # 한팀 마감 -> 새로운 한팀 결성 시작
        cnt = x
print(group)