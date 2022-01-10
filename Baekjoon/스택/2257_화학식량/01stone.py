# 2257 : 화학식량 silver_3
'''
CH(CO2H)3
C         [12]
CH        [12, 1]
CH(       [12, 1, (]
CH(CO     [12, 1, (, 12, 16]
CH(CO2    [12, 1, (, 12, 16*2]
CH(CO2H   [12, 1, (, 12, 32, 1]
CH(CO2H)  [12, 1, 12+32+1]
CH(CO2H)3 [12, 1, 45*3] 148
이런 문제만 있으면 좋겠다...어떻게든 과학하고 연관 좀...
'''

chemical_formula = input()
atom_mass = {'H':1, 'C':12, 'O':16}
stk=[]

for i in chemical_formula:
    
    if i in atom_mass:
        # print(i, atom_mass[i])
        stk.append(atom_mass[i]) # 원자질량 stack에 넣기
    
    elif i == '(':
        stk.append(i)            # 일단 넣음
    
    elif i == ')':               # ) 일 때,
        mass = 0
        while True:
            plus = stk.pop()     
            if plus == '(':      # ( 가 나올 때 까지
                break
            mass += plus         # 내용물 다 더함 
        stk.append(mass)
    
    else:                        # 숫자가 나올때...
        atom = stk.pop()         # 가장 앞에 있는 숫자에 곱함
        stk.append(atom * int(i))

print(sum(stk))
            