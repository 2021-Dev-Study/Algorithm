import sys


mass = {
    'H': 1,
    'C': 12,
    'O': 16
}

str = list(sys.stdin.readline().rstrip())[::-1]
answer = 0

while str:
    temp_num = []
    temp_chem = []
    x = str.pop()
    print(ord(x), x)
    print(ord('A'))

    if x == '(':
        temp_chem.append(x)
        
    elif x == ")":
        temp_chem.append(x)
    

    elif ord(x) >= ord('A') and ord(x) <= ord('Z'):
        if temp_chem:
            temp_chem.append(x)
        else:
            answer += mass[x]
    
    elif ord(x) >= ord('2') and ord(x) <= ord('9'):
        temp = []
        
        for i in range(len(temp_chem)):
            y = temp_chem.pop()
            
            if ord(y) >= ord('A') and ord(y) <= ord('Z'):
                temp.append(mass[y])

            elif ord(y) >= ord('2') and ord(y) <= ord('9'):
                temp.append(int(y) * temp.pop())
            
            elif y == ")":
                answer += (sum(temp) * int(x))
            


