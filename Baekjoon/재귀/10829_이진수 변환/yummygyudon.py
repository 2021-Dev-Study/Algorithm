def make_binary(n,result:list) :
    if n < 2 :
        result.append(str(n%2))
        print(''.join(result[::-1]))
    else :
        result.append(str(n%2))
        make_binary(n//2,result)
result = []
n = int(input())
make_binary(n, result)

## 시간 : 88ms / 메모리 : 30864KB