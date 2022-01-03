# 작성자: red-Pen9uin
# level 7: String
# 5622: 다이얼
"""
상근이의 할머니는 오래된 다이얼 전화기를 사용한다.
전화를 걸고 싶은 번호가 있다면,
숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고,
다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다.
1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며,
한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다.
예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때,
이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

"""
import sys

def get_dial_time(word: str) ->list:
    # 해쉬 테이블과 비슷한 느낌으로,
    # 기존에 생각했던 건 각 다이얼마다 달린 알파벳을 dict 형태로 정리,
    # 검색에 있어서 일일히 비교하는 방식.
    # 다만 너무 오랜 시간이 걸릴 것 같아 solution을 몇 검색했고, 다른 형태로 전환하기로 결정했다.
    string = word.rstrip("\n")
    num_time = list()
    # index[0] -> dial no.2
    dial = ['A', 'D', 'G', 'J', 'M', 'P', 'T', 'W']
    
    for alph in string:
        for i in reversed(range(0, len(dial))):
            if dial[i] <= alph:
                num_time.append(i + 1 + 2)
                break
    return num_time


if __name__ == "__main__":
    dial = sys.stdin.readline()
    print(sum(get_dial_time(dial)))