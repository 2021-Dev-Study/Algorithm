# 스택 (실버 3까지)
# 14713_앵무새


#이거 답은 똑같이 나오는데 실패...
import sys

if __name__ == "__main__":
    
    N = int(input())
    str = [0] * N 
    for i in range (N):
        str[i] = sys.stdin.readline().split()

    L = input().split()

    # 각 앵무새가 말한 단어들을 스택에 저장하고
    # cseteram이 받아 적은 단어들을과 비교해서 같으면 스택에서 꺼내기
    for word in L:
        for i in range (N):
            while str[i]:
                if word == str[i][0] :
                    str[i].pop(0)
                else:
                    break
    
    # 각 앵무새의 스택이 전부 비어있으면 Possible 출력
    sum = 0
    for i in range(N):
        sum += len(str[i])

    if sum == 0:
        print("Possible")
    else:
        print("Impossible")



