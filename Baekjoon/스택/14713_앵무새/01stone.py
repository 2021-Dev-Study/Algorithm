# 14713	: 앵무새 silver_3
'''
- 한 앵무새는 한 문장을 기억하고 있다. 
    문장은 여러 단어로 이루어져 있는데, 앵무새는 이 단어들을 순서대로 말한다.
- 한 앵무새가 단어를 말하고 그다음 단어를 말하기 전에는 약간의 간격이 있는데, 
    이때 다른 앵무새가 말을 가로채고 자신의 문장을 말할 수 있다.
- 한 앵무새가 단어를 말하는 도중에는, 다른 앵무새가 말을 가로채지 않는다.
- 어떤 단어도 앵무새가 말하는 모든 문장을 통틀어 2번 이상 등장하지 않는다.
'''

'''
[[i want to see you], [next week], [good luck]]
[i want next good luck week to see you]

you   [i want to see], [next week], [good luck] - [you]
see   [i want to],     [next week], [good luck] - [you see]
to    [i want],        [next week], [good luck] - [you see to]
week  [i want],        [next],      [good luck] - [you see to week]
luck  [i want],        [next],      [good]      - [you see to week luck]
good  [i want],        [next],      []          - [you see to week luck good]
next  [i want],        [],          []          - [you see to week luck good next]
want  [i],             [],          []          - [you see to week luck good next want]
i     [],              [],          []          - [you see to week luck good next want i]
'''


n = int(input())
parrots = []
for i in range(n):
    l = list(input().split())
    parrots.append(l)

dictation = list(input().split())

stk = []
for word in dictation[::-1]:
    for i in range(n):
        if parrots[i] and word == parrots[i][-1]: # i번째 앵무새가 말한 마지막 단어와 일치하면
            stk.append(parrots[i].pop())          # 스택에 넣음
            break
# print(stk)

if dictation == stk[::-1]:
    print('Possible')
else:
    print('Impossible')


