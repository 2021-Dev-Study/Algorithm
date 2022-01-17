import sys


mass = {
    'H': 1,
    'C': 12,
    'O': 16
}

str = list(sys.stdin.readline().rstrip())[::-1]
print(str)
answer = 0

while str:
    temp_num = []
    temp_chem = []
    x = str.pop()
    
    if x == '(':
        temp_chem.append(x)
        print(temp_chem)
        
    elif x == ")":
        temp_chem.append(x)
    

    elif ord(x) >= ord('A') and ord(x) <= ord('Z'):
        if temp_chem:
            temp_chem.append(x)
        else:
            answer += mass[x]
    
    elif x in '23456789':
        temp = []

        while temp_chem:
            y = temp_chem.pop()
            print(y)
            if y in "HCO":
                temp.append(mass[y])

            elif ord(y) >= ord('2') and ord(y) <= ord('9'):
                temp.append(int(y) * temp_chem.pop())
            
            elif y == "(":
                answer += (sum(temp) * int(x))
print(answer)        


