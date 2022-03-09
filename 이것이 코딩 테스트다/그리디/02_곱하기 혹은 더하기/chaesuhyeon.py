arr = list(input())

result = int(arr[0])

for i in range(1,len(arr)):

    n = int(arr[i])
    if result <= 1 or n  <= 1:
        result += n
    else:
        result *= n    
print(result) 
