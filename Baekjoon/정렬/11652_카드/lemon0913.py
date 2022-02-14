# 정렬
# 11652_카드
import sys
if __name__ == "__main__":
    N = int(input())
    # 입력받은 카드의 수를 dictionary에 저장
    # dic의 Key는 정수, Value는 해당 정수가 몇 번 나왔는지
    dic = {}
    for i in range(N):
        card = int(sys.stdin.readline())
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    
    # dic의 Value를 내림차순으로 정렬하고 동일 값에 대해서 Key를 오름차순으로 정렬
    result = sorted(dic.items(), key = lambda x:(-x[1], x[0]))
    print(result[0][0])
    