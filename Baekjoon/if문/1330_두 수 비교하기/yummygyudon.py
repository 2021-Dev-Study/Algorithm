# 문제
# 두 수 비교하기
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
#
# 출력
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
#
# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# 제한
# -10,000 ≤ A, B ≤ 10,000

# string type이지만 ASCII 코드값 -> 대소비교 가능
def compare(x) :
    a = x.split(' ')[0] # 공백을 기준 분리한 결과 리스트의 첫 번째값
    b = x.split(' ')[1] # 공백을 기준 분리한 결과 리스트의 두 번째값
    if a > b :
        result = '>'
    elif a < b :
        result = '<'
    else :
        result = '=='
    return result

print(compare('1 2'))

# 아.. 함수로 만드는게 아니고 input을 사용해야하나봅니다...

a, b = map(int, input().split(' ')) #map 함수로 split한 두 개의 요소 한번에 숫자형으로 바꿔주기
if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print('==')
