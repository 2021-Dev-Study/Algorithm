# 크로아티아 알파벳

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, '*') # 크로아티아 문자를 *(1개)로 치환해버림

print(len(word))