# 다이얼

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
sec = 0

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            sec += dial.index(j) + 3
            # 다이얼 돌릴 때 1을 누르는데 2초 + 이후 1초 씩 증가, index는 0부터

print(sec)