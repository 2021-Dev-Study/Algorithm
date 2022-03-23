S = input()

n = len(S)

result = []
#n//2 +1
for i in range(1,n+1):
    cnt = 1
    tmp = ''
    s = S[:i]
    # print(s)
    for k in range(i,n,i):
        if s == S[k:k+i] :
            cnt += 1
        else :
            if cnt < 2 :
                tmp += s
            else :
                tmp += (str(cnt)+s)
            s = S[k:k+i]
            cnt =1
    ### 여기 빠뜨리면 개고생합니당~
    # 왜 계속 aabb 단위인 단계에서 뒤에 acc가 안들어갈까 했는데 이거 때문이였네요
    if cnt < 2:
        tmp += s
    else:
        tmp += (str(cnt) + s)
    # print(tmp)
    # print()
    result.append(tmp)
result.sort(key = lambda x: len(x))
# for r in result
print(len(result[0]))
