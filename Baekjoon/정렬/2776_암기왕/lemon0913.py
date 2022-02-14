# 정렬
# 2776_암기왕
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        list1 = list(map(int, input().split()))
        M = int(input())
        list2 = list(map(int, input().split()))

        # 수첩1에 적어놓은 정수를 dictionary로 변환
        # dic의 Key값은 수첩에 적은 정수, Value는 1
        dic = {}
        for i in list1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        # 수첩2에 적은 정수가 dic안에 존재하면 1을 출력, 존재하지 않으면 0을 출력
        for i in list2:
            result = dic.get(i)
            if result == None:
                print(0)
            else:
                print(1)
    