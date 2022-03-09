arr = input()
zero = 0
one = 0

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        if  arr[i+1] == '0':
            one += 1
        else:
            zero += 1

print(min(zero, one)) 

