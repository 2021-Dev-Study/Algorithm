## 11650/11651 좌표정렬하기 풀이방법과 유사
import sys
N = int(sys.stdin.readline())
ls = []
#단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
# set로 먼저 중복 제거
words =set()
for i in range(N) :
    word = sys.stdin.readline().rstrip()
    words.add(word)
for w in words :
    ls.append((len(w), w))
# 문자열을 sorted하면 자동으로 사전순으로 정렬됨.
s_words = sorted(ls, key= lambda x : (x[0], x[1]))
for w in s_words :
    print(f"{w[1]}")