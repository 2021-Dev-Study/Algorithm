# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 각각의 알파벳에 대해서,
# a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를
# 공백으로 구분해서 출력한다.
#
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# index를 가져오는건 쉬운데 순서 생각하는게 쉽지않았네요
import sys,string
s = str(sys.stdin.readline().rstrip())
alphabets = string.ascii_lowercase[:]
for alp in alphabets : # 전체 알파벳을 모두 조회해야되기 때문에 alphabets으로 for문
    if alp in s: #각 알파벳들이 만약 입력문자열 안에 있으면
        print(s.index(alp),end=' ') # 입력문자열에서의 위치 가져오고
    else :
        print(-1, end=' ') # 없으면 -1



