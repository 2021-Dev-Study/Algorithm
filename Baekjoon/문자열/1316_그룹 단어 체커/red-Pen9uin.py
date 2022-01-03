# 작성자: red-Pen9uin
# level 7: String
# 1316: 그룹 단어 체커
"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다.

예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

"""
import sys

if __name__ == "__main__":
    case = int(sys.stdin.readline())
    g_word = 0

    for _ in range(0, case):
        word = sys.stdin.readline().rstrip("\n")

        alph = list()
        before = word[0]
        alph.append(before)
        is_group = True
        
        for i in range(1, len(word)):
            now = word[i]
            # 새로운 문자의 등장
            if now != before:
                #만약 이전에 있었던 문자라면 False
                if now in alph :
                    is_group = False
                    break
                else:
                    alph.append(now)
            before = now
        
        # 무사히 통과할 경우
        if is_group:
            g_word += 1
    
    print(g_word)
