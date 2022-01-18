# 12034	: 김인천씨의 식료품가게 (Large)

'''
# 런타임 에러
t = int(input())
answer = []

for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    stk_dis = []

    while len(stk_dis) != n:               # n개까지만
        price_dis = price.pop(0)          
        if price_dis//0.75 in price:       # 할인된 가격이 이미 가격표에 있다면
            price_dis.append(stk_dis)      # 할인한 stk에 넣음
            price.remove(price_dis//0.75)  # 기존에는 제거
    
    answer.append(stk_dis)
    print("Case #%d: %s" % (i+1, " ".join(answer)))
'''


t = int(input())

for i in range(1, t+1) :
  n = int(input())
  bill = sorted(map(int, input().split()), reverse=True)
  discount = []

  while bill :
    price = bill.pop()

    if price * 4//3 in bill :
      discount.append(str(price))
      bill.remove(price * 4//3)

  print("Case #%d: %s" % (i, " ".join(discount)))








'''
for itc in range(int(input())):
    input()
    r = []
    b = []
    i = 0
    for v in map(int, input().split()):
        if len(b) > i and v == b[i]:
            i += 1
        else:
            r.append(v)
            b.append(v // 3 * 4)
    print('Case #{}:'.format(itc + 1), *r)
'''