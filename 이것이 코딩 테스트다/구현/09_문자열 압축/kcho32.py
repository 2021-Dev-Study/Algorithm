# 총 길이의 반까지 단위로 만들 수 있음 -> 그 이상은 압축이 안됨
# 1 글자, 2 글자, 3 글자 ... 순으로 단어 압축 시도
from collections import deque

string = input()
zip_unit = 1 # 단어 압축 단위
zip_unit_length = []

while len(string):
    if zip_unit > len(string) // 2:
        break

    tmp = deque()

    for i in range(0, len(string) - zip_unit + 1, zip_unit):
        tmp.append(string[i:i+zip_unit])
    if i + zip_unit < len(string):
        tmp.append(string[i+zip_unit:])
        
    shorted_str = ""
    ch = tmp.popleft()
    cnt = 1

    while tmp:
        if ch == tmp[0]:
            cnt += 1
            tmp.popleft()
        else:
            if cnt == 1:
                shorted_str += ch
            else:
                shorted_str += str(cnt) + ch
            ch = tmp.popleft()
            cnt = 1
    if cnt == 1:
        shorted_str += ch
    else:
        shorted_str += str(cnt) + ch

    zip_unit_length.append(len(shorted_str))
    zip_unit += 1

if len(string) == 1:
    print("1")
else:
    zip_unit_length.sort()
    print(zip_unit_length[0])