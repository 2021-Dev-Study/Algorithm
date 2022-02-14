# collection 모듈 most_common으로 할 수 있긴한데 허무할 것 같아서,,
# 이전 스터디때 활용했던 dictionary를 사용해볼까 합니다.
import sys
n = int(sys.stdin.readline())
# for문이 3번이나 들어가서 비효율적인 듯
# sales=[]
# for _ in range(n):
#     sale = sys.stdin.readline().rstrip()
#     sales.append(sale)
# book = list(set(sales))
# cnt = []
# d = {b : sales.count(b) for b in book}
# best = max(d.values())
# best_seller = []
# for b, s in d.items() : #
#     if s == best :
#         best_seller.append(b)

sales = {}
for _ in range(n):
    sale = sys.stdin.readline().rstrip()
    if sale in sales : # dict 내에 이미 책이 등록되어있으면
        sales[sale] += 1 # 1 더해주고
    else : # 없으면
        sales[sale] = 1 # 등록해주기
best = max(sales.values()) # 최대 판매량을 .values에서 추출
best_seller = []
for b, s in sales.items() : # 판매량이 같은 경우 대비
    if s == best :
        best_seller.append(b) # 사전순 정렬이 필요하기 때문에 책이름만 append

print(sorted(best_seller)[0]) # 책이름들로만 sorted -> 사전순


# 람다 함수 활용 실패...
# book = set(sales)
# cnt = [(sales.count(b), b) for b in book ]
# s_sales = sorted(cnt, key= lambda x : x[0],reverse=True)
# max = s_sales[0][0]
# best = []
# for i in range(len(s_sales)) :
#     if s_sales[0][0] == max :
#         best.append(s_sales[0][0])
# print(sorted(best, key= lambda x : x[1])[0][1])
