target_count = int(input())
count = 1
title = 666 # 초기 영화 제목은 666부터 시작

while True:
    if "666" in str(title):
        count += 1
    
    if count == target_count + 1:
        break

    title += 1   

print(title)