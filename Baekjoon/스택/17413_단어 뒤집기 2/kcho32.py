import sys


answer = ""
str = list(sys.stdin.readline().rstrip()[::-1])
word = []
temp = []
word = []
print(str)
while str:
    x = str.pop()
    if x == "<":
        if word:
            answer += "".join(word[::-1])
            word = []
        temp.append(x)
    elif x == ">":
        temp.append(x)
        answer += "".join(temp)
        temp = []
    elif x == " ":
        if word and not temp:
            answer += "".join(word[::-1])
            answer += x
            word = []
        elif not word and temp:
            temp.append(x)
    else:
        if not temp:
            if str:
                word.append(x)
            else:
                word.append(x)
                answer += "".join(word[::-1])
        else:
            temp.append(x)

print(answer)



