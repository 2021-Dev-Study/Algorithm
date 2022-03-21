S = input()

n = len(S)

result = []
for i in range(1,n//2 +1): # 끝을 n+1 로 계속 생각했는데 안되는 이유가 하위 for문에서 s 의 다음 범위부터 비교하는데 i가 문자열의 범위를 벗어나면
                        # 압축불가로 그자체가 tmp로 되어야하는데 else문에 빠지면서  tmp에는 압축단위인 처음 s만 들어갈 수 밖에 없게된다
    cnt = 1
    tmp = ''
    s = S[:i]
    print(s)
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
    print(tmp)
    print()
    result.append(tmp)
result.sort(key = lambda x: len(x))
# for r in result
print(len(result[0]))
