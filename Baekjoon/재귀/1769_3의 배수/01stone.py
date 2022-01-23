# 1769 : 3의 배수

'''
n = '1234'
sum = 0
for i in n:
  sum = sum + int(i)
print(sum)    # 10
print(len(n)) # 4
'''

cnt = 0
def function(n):
    # cnt = 0 여기다가 하면 안세짐...
    global cnt
    if len(n) > 1:
        sum = 0
        for i in n:
            sum += int(i)
        x_again = str(sum)
        cnt += 1
        function(x_again)
   
    else:        
        if int(n) % 3 == 0:
            print(cnt, '\nYES')
        else:
            print(cnt, '\nNO')


n = input().rstrip()
function(n)