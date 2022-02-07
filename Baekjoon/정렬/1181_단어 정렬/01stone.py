# 1181 : 단어 정렬

n = int(input())
words = [str(input()) for i in range(n)]
words = list(set(words))

# lambda : 익명함수
# lambda 인자(words의 인자) : 표현식((글자수, 글자)) 
# key = 정렬을 목적으로 하는 함수를 값으로 넣음
words.sort(key = lambda x : (len(x), x))

print('\n'.join(words))