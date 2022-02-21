s = input().rstrip()
tag = False
word = ''
answer = ''

for i in s:
    if tag == False:
        if i == '<':
            tag = True
            word += i
        elif i == " ":
            word += i
            answer += word
            word = ''
        else:
            word = i + word
    else:
        word += i
        if i == '>':
            tag = False
            answer += word
            word = ''

print(answer+word)