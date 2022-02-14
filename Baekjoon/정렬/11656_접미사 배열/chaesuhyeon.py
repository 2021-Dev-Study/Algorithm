import sys
word = list(sys.stdin.readline().rstrip()) # word  :  ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
arr = []
tmp = "" 
for _ in range(len(word)): # 단어의 길이만큼 반복
    p = word.pop() # 맨 끝 원소 뽑음
    tmp = p + tmp # 뽑은 맨끝원소를 기존 접미사와 계속 더해줌 (순서 p먼저 주의)
    arr.append(tmp) # 합친 단어를 리스트에 append

arr.sort() # 정렬 

for i in arr: # 리스트 원소 뽑아줌
    print(i)
