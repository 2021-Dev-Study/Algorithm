data = input().split('-') # 55-50+40 --> ['55', '50+40']

num=[]

for i in data:
    result = 0
    p = i.split('+')

    for j in p:
        result += int(j)
    num.append(result)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)

# 55-50+40
# p :  ['55']
# result:  55
# p :  ['50', '40']
# result:  90
# -35

# 10+20+30+40
# p :  ['10', '20', '30', '40']
# result:  100
# 100

# 00009-00009
# p :  ['00009']
# result:  9
# p :  ['00009']
# result:  9
# 0
