# 정렬
# 10815_숫자 카드

import sys
if __name__ == "__main__":
    N = int(input())
    listN = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    listM = list(map(int, sys.stdin.readline().split()))

    # listN으로 딕셔너리 만들기
    # Key는 listA의 원소, Value는 1
    dic = {}
    for i in listN:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # listM의 원소가 딕셔너리에 Key값으로 존재하면 1 출력
    # 존재하지 않으면 0 출력    
    for i in listM:
        result = dic.get(i)
        if result == None:
            print(0, end=' ')
        else:
            print(1, end=" ")
