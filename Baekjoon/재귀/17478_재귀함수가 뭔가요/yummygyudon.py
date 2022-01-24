def print_message(n,cnt=0):
    if cnt == n :
        bar = "____" * cnt
        print(f'{bar}"재귀함수가 뭔가요?"')
        print(f'{bar}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{bar}라고 답변하였지.')
        cnt-=1
        return cnt
    bar = "____"*cnt
    print(f'{bar}"재귀함수가 뭔가요?"')
    print(f'{bar}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f"{bar}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(f'{bar}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    cnt+=1
    print_message(n,cnt)
    bar = "____" * (cnt-1) # bar 0개일 때를 위해서 재귀 종료때 답변하였지 출력하고 재귀될땐 cnt-1씩
    print(f'{bar}라고 답변하였지.')

n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
print_message(n)