import sys
N = int(sys.stdin.readline().rstrip())
word = [] # 문자와 길이를 담을 리스트
array = [] # 문자 중복 체크를 위한 리스트 
cnt = 0 # 문자 개수 체크 

for _ in range(N):
    alpha = sys.stdin.readline().rstrip()
    if alpha not in array: # 입력한 문자가 array에 없다면 
        array.append(alpha) # array에 append
        length = len(alpha) # 입력받은 문자 길이 체크 
        word.append([alpha, length]) # word에 문자와 길이를 리스트로 append (이중배열)
        cnt += 1

word.sort(key=lambda z: (z[1], z[0])) # 문자의 길이를 기준으로 정렬 

for i in range(cnt): # 추가된 문자숫자만큼 반복 (중복 제거한 개수)
    print(word[i][0]) # word에서 문자만 출력 


# 개선한 풀이 
words = []
N = int(sys.stdin.readline().rstrip())
for i in range (N):
    words.append(input())

words = list(set(words)) # set을 이용해서 문자열 제거한 뒤 list로  변환 
words.sort() # 문자 알파벳 순서대로 정렬

words = sorted(words, key=lambda word:len(word)) # lamda를 이용해서 문자 길이를 기준으로 정렬 
for i in range (len(words)):
    print(words[i]) # 정렬된 문자 출력 