# 그룹단어체커

num = int(input())
count = num

for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word.find(word[j]) > word.find(word[j+1]): # 중복 문자가 있었다면
            count -= 1
            break

print(count) # 5개월 전의 내가 더 똑똑한 것 가틍ㄴㄷ..저거 어떻게 생각했지..