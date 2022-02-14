import sys


answer = ""
str = list(sys.stdin.readline().rstrip()[::-1])
word = []
temp = []
print(str)
while str:
    x = str.pop()
    ## < 태그 시작이 나왔을 때 word에 단어가 있으면 있는 단어를 answer문자열에 거꾸로 넣어줌
    ## 그리고 temp에 push
    ## > 태그 끝이 나왔을 때에는 순서 바꾸지 않고 answer문자열에 더해줌
    if x == "<":
        if word:
            answer += "".join(word[::-1])
            word = []
        temp.append(x)
    elif x == ">":
        temp.append(x)
        answer += "".join(temp)
        temp = []
    ## 띄어쓰기 나오고 태그 없었다면 word에 있는 것을 역순으로 문자열 answer로 더해줌
    ## 태그가 있으면 태그 temp에 push
    elif x == " ":
        if word and not temp:
            answer += "".join(word[::-1])
            answer += x
            word = []
        elif not word and temp:
            temp.append(x)
    ## 문자가 나올경우, temp가 차있으면 temp에 push
    ## 비어있고 str이 남아있다면 word에 push, str 다 줄어들면 다시 역순으로 출력

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



