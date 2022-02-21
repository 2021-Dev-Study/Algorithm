n = int(input())
count = 0
num = 666
while True:
    if '666' in str(num): # num에 1값을 더해줘야하기때문에 기본형은 int이고 str로 바꿔서 '666'이 포함되어 있는지 확인한다.
        count += 1
    if count == n:
        print(num)
        break
    num += 1

# num을 1씩 증가시켜서 666이 문자열안에 포함되어 있다면 count를 +1 해주고
# count값과 n이 동일하다면 그때의 종말 숫자를 출력 해준다.