# 셀프넘버가 아닌 숫자를 구한 후 전체에서 아닌 숫자 빼주기
# 아이디어는 구했는데 while문 부분 코드를 어려워서 참고함.

def self_number(number):
    self_number = number
    while number != 0:
        self_number += number%10
        number //= 10
    return self_number     # 생성자가 있는 숫자를 리턴해줌
        
array = []

for i in list(range(1,10001)):
    array.append(self_number(i))  # 리스트에 생성자가 있는 숫자들을 추가
    if i not in array:  #배열에 없는 i이면 i를 출력해라
        print(i)