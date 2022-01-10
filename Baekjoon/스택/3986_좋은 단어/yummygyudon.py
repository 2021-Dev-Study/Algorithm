# 도저히 어디가 틀린건지 모르겟습니다...같이 봐주세요,....ㅠㅜ
import sys

n = int(sys.stdin.readline())
cnt =0
for _ in range(n) :
    stk = []
    ptr = 0
    s = sys.stdin.readline().rstrip()
    for chr in s :
        if len(stk) == 0 : # 아무것도 없을 때
            stk.append(chr) # 새롭게 알파벳 삽입
            ptr += 1 # 1개가 들어왔다는 의미로 1
        elif stk[-1] == chr : # 직전값이 같으면 다른선과 겹칠 일이 없기때문에
            stk.pop() # 쌍으로 없애주기 (append 안하고 직전값 빼주기)
            ptr -= 1 # 직전값없앴으니 ptr 1 빼주기
        else : # 직전값과 다를 때
            if ptr > 1 : # (stk : [A,B], 입력 : A이거나  [B,A], 입력 : B일 때) 선이 겹칠 수 밖에 없는 상황
                break # ptr이 2인 채로 종료
            else : # 아직 stk에 알파벳이 하나 밖에 없을 때 (stk : [A], 입력 : B이거나  [B], 입력 : A일 때)
                stk.append(chr) # 그 다음 입력까지 봐야 짝이 될지 알수 있기때문에 일단 append
                ptr += 1 # 위 if문에서 효과를 보기위한 ptr + 1
                # 다음 입력값이 만약 이번 값과 같으면 .pop되어서 없어질 수 있음
    if ptr == 0 and len(stk) == 0 :
        cnt+=1
print(cnt)

# ex
# ABBABAAAAB라고 했을 때
# AB -> ABB에서 BB 사라짐 -> A(BB)
# A(BB)A -> AA 사람짐 -> stk은 빈 상태 (ABBA)
# (ABBA)B ->(ABBA)BA : ptr 2-> (ABBA)BAA -> (ABBA)B(AA) ptr :1 -> (ABBA)B(AA)A ptr :2
# (ABBA)B(AA)AA -> (ABBA)B(AAAA) ptr : 1 -> (ABBA)B(AAAA)B -> (ABBABAAAAB) ptr : 0
# ptr은 0이 되기때문에 모두 짝지어 없어진 상황 -> cnt += 1