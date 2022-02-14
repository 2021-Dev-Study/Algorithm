# 정렬
# 1764_듣보잡

# 역시 시간초과...풀면서 시간초과 날 것 같았다...ㅎ
# import sys
# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     listN = [0] * N
#     listM = [0] * M

#     for i in range(N):
#         listN[i] = sys.stdin.readline().replace("\n", "")
    
#     for i in range(M):
#         listM[i] = sys.stdin.readline().replace("\n", "")

#     # listN의 원소가 listM에도 있다면 그 원소를 Nonelist에 추가하고 count를 1 증가시키기 
#     Nonelist = []
#     count = 0
#     for i in range(len(listM)):
#         for j in range(len(listN)):
#             if listM[i] == listN[j]:
#                 count += 1
#                 Nonelist.append(listM[i])
    
#     print(count)
#     for i in Nonelist:
#         print(i)


# 두 명단의 교집합을 구하는 문제 -> 집합을 사용하라
if __name__ == "__main__":
    N, M = map(int, input().split())

    setN = set()
    for i in range(N):
        setN.add(input())
    
    setM = set()
    for i in range(M):
        setM.add(input())
    
    # setN과 setM의 교집합을 구해 오름차순으로 정렬
    result = sorted(list(setN & setM))
    
    print(len(result))
    for i in result:
        print(i)



