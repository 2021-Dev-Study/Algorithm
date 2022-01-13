# 작성자: red-Pen9uin
# Data structure: stack
# 3956: 좋은 단어
# 수행 결과: 30864 KB / 112 ms
"""
이번 계절학기에 심리학 개론을 수강 중인 평석이는 오늘 자정까지 보고서를 제출해야 한다.
보고서 작성이 너무 지루했던 평석이는 노트북에 엎드려서 꾸벅꾸벅 졸다가 제출 마감 1시간 전에 깨고 말았다.
안타깝게도 자는 동안 키보드가 잘못 눌려서 보고서의 모든 글자가 A와 B로 바뀌어 버렸다!
그래서 평석이는 보고서 작성을 때려치우고 보고서에서 '좋은 단어'나 세보기로 마음 먹었다.

평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다.
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면,
그 단어는 '좋은 단어'이다.
평석이가 '좋은 단어' 개수를 세는 것을 도와주자.

"""
import sys


def is_good(word: str) ->int:
    stack = list()
    cnt = -1
    for i in word:
        if (cnt >= 0):
            if stack[cnt]!=i:
                stack.append(i)
                cnt += 1
            else: # stack[cnt]==i
                del stack[cnt]
                cnt -= 1
        else: #  cnt < 0
            stack.append(i)
            cnt += 1
    
    if cnt == -1:
        return 1
    else:
        return 0    


if __name__ == "__main__":
    cnt = int(sys.stdin.readline())
    good_word = 0

    for _ in range(cnt):
        word = sys.stdin.readline().rstrip('\n')
        good_word += is_good(word)

    print(f"{good_word}")