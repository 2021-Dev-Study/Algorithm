s_num = list(input())
result = 0
for n in s_num :
    num = int(n)
    if result == 0 or num <= 1 :
        result += num
    else :
        result *= num
print(result)
