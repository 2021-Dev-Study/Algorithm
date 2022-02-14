# 정렬
# 10816_숫자 카드 2

# 이건 시간초과...
# import sys
# if __name__ == "__main__":
#     N = int(input())
#     listA = list(map(int, sys.stdin.readline().split()))
#     M = int(input())
#     listB = list(map(int, sys.stdin.readline().split()))

#     # listB의 원소들이 listA에 몇 개 있는지 세서 출력
#     for i in listB:
#         print(listA.count(i), end = ' ')


    
# 그래서 Counter 클래스를 사용해봄
# 근데 이것도 시간초과....ㅎ
# from collections import Counter
# import sys
# if __name__ == "__main__":
#     N = int(sys.stdin.readline())
#     listA = list(map(int, sys.stdin.readline().split()))
#     M = int(sys.stdin.readline())
#     listB = list(map(int, sys.stdin.readline().split()))

#     count = Counter(listA)
#     for i in range(len(listB)):
#         if listB[i] in listA:
#             print(count[listB[i]], end=' ')
#         else:
#             print(0, end=' ')


# 이번에는 Counter대신 dictionary를 사용해보자
import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    listA = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    listB = list(map(int, sys.stdin.readline().split()))

    # listA로 딕셔너리 만들기
    # Key는 listA의 원소, Value는 listA에 해당 원소가 몇 개 있는지
    dic = {}
    for i in listA:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # listB의 원소가 딕셔너리에 Key값으로 존재하면 Value 출력
    # 존재하지 않으면 0 출력
    for i in listB:
        result = dic.get(i)
        if result == None:
            print(0, end=' ')
        else:
            print(result, end=' ')    