x = int(input())

if x % 4 == 0:
    if x % 100 != 0:
        print(1)
    elif x % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)



#연도는 1보다 크거나 같고, 4000보다 작거나 같다는 조건을 어떻게 표현하나.....

#조건을 잘못이해했네..
#if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0): 이라는 소리임  