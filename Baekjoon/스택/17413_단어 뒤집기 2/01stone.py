# 17413	: 단어 뒤집기 2 silver_3
'''
태그 안은 정방향, 태그 바깥은 역방향
'''
# 2257하고 비슷하게 풀면 될듯?

'''
# trial

stk = []
for i in input():
         
    if i == '>':              
        tag = []
        while True:
            plus = stk.pop()     
            if plus == '<':      
                break
            tag.append(plus)        
        stk.append('<' + ''.join(tag[::-1]) + '>')
    
    else:                               
        stk.append(i)

print(stk) # ['<ab cd>', 'f', 'e', ' ', 'h', 'g', '<ij kl>'] 
           # 여기서부터 뭔가 잘못됨을 감지..
           # 합칠 때 저 낱개도 공백 기준으로 같이 합쳤어야 함...

<ab cd>fe hg<ij kl> tag  [word]   [answer]
<                    T   [<]      []
<ab cd               T   [<ab cd] []  
<ab cd>              F   []       [<ab cd>]
<ab cd>fe hg         F   [gh ef]  [<ab cd>]
<ab cd>fe hg<        T   [<]      [<ab cd>gh ef]
<ab cd>fe hg<ij kl   T   [<ij kl] [<ab cd>gh ef]
<ab cd>fe hg<ij kl>  F   []       [<ab cd>gh ef<ij kl>]
'''

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

print(answer + word) #print(answer)는 틀림 
