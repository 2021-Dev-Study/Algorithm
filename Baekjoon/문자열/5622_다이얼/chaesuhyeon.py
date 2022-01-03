# 알파벳에 숫자를 먼저 할당해주고 걸리는 시간은 (숫자 +1)초임
# 문자만 입력하기 때문에 0과 1은 생각할 필요가  X
 
A = input()
alpha = " "
sum = 0
for a in A:
    if a == "A" or a == "B" or a == "C":
        alpha = "2"
    elif a == "D" or a == "E" or a == "F":
        alpha = "3"
    elif a == "G" or a == "H" or a == "I":
        alpha = "4"
    elif a == "J" or a == "K" or a == "L":
        alpha = "5"
    elif a == "M" or a == "N" or a == "O":
        alpha = "6"
    elif a == "P" or a == "Q" or a == "R" or a == "S":
        alpha = "7"
    elif a == "T" or a == "U" or a == "V":
        alpha = "8"        
    elif a == "W" or a == "X" or a == "Y" or a == "Z":
        alpha = "9"   
    
    sum += (int(alpha)+1)
    
print(sum)

##############################################################################
# 찾아본 풀이
Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
A = list(input())
time = 0 # 걸리는 시간 
for a in A:
    for n in Number:
        if a in n:
            time += Number.index(n) + 3 # index에 3초를 더해줘야 시간나옴
print(time)