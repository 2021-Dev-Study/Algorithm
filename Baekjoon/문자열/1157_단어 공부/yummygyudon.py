# 문제
# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

from collections import Counter

v = [alp for alp in input().upper()] # 대문자 출력 조건이기때문에 먼저 upper 해주기
c = Counter(v) # 리스트에 각 요소별 빈도값을 튜플형 _ [(value, count),...]으로 생성
mst =  c.most_common() # 빈도값 정렬
max = mst[0][1] # 맨앞값이  최빈값 튜플이기때문에 최빈값 index로 최빈값 변수에 대입

# 최빈값이 중복될 때 대비
max_alps = []
for cnt in mst :
    if cnt[1] == max:
        max_alps.append(cnt[0])

if len(max_alps) == 1 : # 최빈값을 가진 값이 하나일 땐 해당 알파벳 출력
    print(max_alps[0]) # 빈도수 말고 알파벳 출력
else :
    print('?')