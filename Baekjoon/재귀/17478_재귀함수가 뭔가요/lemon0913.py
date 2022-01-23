# 재귀 (단계별 & 실버5)
# 17478_재귀함수가 뭔가요?

def answer(n, count):
    if count < n*4: # count < n*4면 _와 문구를 출력
        print("_"*count + "\"재귀함수가 뭔가요?\"")
        print("_"*count + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print("_"*count + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("_"*count + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        count += 4
        answer(n, count)
        count -= 4 # 앞에서 count를 증가시켰기때문에 이전과 _ 수를 일치시키려면 다시 count 감소시키기
        print("_"*count + "라고 답변하였지.")

    else: # count == n*4면 _와 다른 문구를 출력
        print("_"*count + "\"재귀함수가 뭔가요?\"")
        print("_"*count + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print("_"*count + "라고 답변하였지.")




if __name__ == "__main__":
    N = int(input())
    cnt = 0
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    answer(N, cnt)



# 왜 이게 실버5고 이진수 변환이 브론즈 2..??