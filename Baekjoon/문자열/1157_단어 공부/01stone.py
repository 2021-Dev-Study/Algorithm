# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 
# 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
'''
입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
       주어지는 단어의 길이는 1,000,000을 넘지 않는다.
출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
       단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 
       ?를 출력한다.
'''

word = input().upper()      # 다 대문자
word_set = list(set(word))  # 중복 제거

num = []  # 알파벳 당 갯수
for i in word_set :
    num.append(word.count(i))  

if num.count(max(num)) > 1 : # 최댓값이 여러개면 ? 출력
    print('?')
else :
    max_index = num.index(max(num))
    print(word_set[max_index])