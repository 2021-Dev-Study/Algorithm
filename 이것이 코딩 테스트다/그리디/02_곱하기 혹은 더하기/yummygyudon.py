s_num = list(input())
result = 0
for n in s_num :
    num = int(n)
    if result <= 1 or num <= 1 :
        # == 으로 하게 되면 result가 1일 경우, 1(result)을 곱하게 됨.
        result += num
    else :
        result *= num
print(result)
