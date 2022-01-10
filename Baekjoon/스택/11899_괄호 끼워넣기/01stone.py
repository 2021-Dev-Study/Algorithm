# 11899	: 괄호 끼워넣기 silver_4
'''
올바른 괄호열으로 만들기 위해 앞과 뒤에 붙여야 할 괄호의 최소 개수를 구하는 프로그램을 작성하세요.
'''
# 짝 맞춰서 그냥 소거해도 될 듯? 스택 영~ 안 익숙해지네..

s = input().rstrip()
len_s = len(s)
s_del = s

while True:
    s_del = s_del.replace("()",'') # 한 번에 하나만 지움
    len_s -= 1
    if len_s == 0:
        print(len(s_del))
        break

