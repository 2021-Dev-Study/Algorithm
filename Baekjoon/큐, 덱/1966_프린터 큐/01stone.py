# 1966 : 프린터 큐
# 고민해봤지만~!! 모르겠어서 답 찾아봤슴니다~!~!~!~!하하하하핳

T = int(input())
 
for _ in range(T):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    index = [i for i in range(n)]
    index[m] = 'target'    # 내가 찾고 싶은 index
    cnt = 0
 
    while priority:
        if priority[0] == max(priority):    # 나머지 문서들보다 중요도가 더 높은 문서가 없다면
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            priority.pop(0)
            index.pop(0)
        else:
            priority.append(priority.pop(0))
            index.append(index.pop(0))