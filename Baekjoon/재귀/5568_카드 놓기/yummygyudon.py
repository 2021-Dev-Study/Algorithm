# 모든 숫자들을 순서대로 만들고 세트에 계속 넣으면 알아서 중복값 제거할 듯
import sys
# 첫번째 예제는 성공
#카드를 3장 이상 뽑았을 때 오류 발생 while문
# 아 어렵네요...
# 다들 백트래킹으로 풀었다는데 저도 백트래킹을 배워와야할듯...
def make_number(card :list, set : set, select) :
    if len(card) < select :
        print(len(set))
    else :
        idx = 0
        main = card.pop()
        while idx <= len(card)-(select-1) :
            num1 = ''.join([str(main),str(card[idx])])  #뒤에 붙인 수
            set.add(num1)
            num2 = ''.join([str(card[idx]),str(main)])  #앞에붙인 수
            set.add(num2)
            idx += 1

        make_number(card,set,select)


ea = int(sys.stdin.readline().rstrip())
select = int(sys.stdin.readline().rstrip())
card = []
for _ in range(ea):
    card.append(int(sys.stdin.readline().rstrip()))
s = set()
make_number(card, s, select)