# 작성자: red-Pen9uin
# level 7: String
# 1152: 단어의 개수
"""
영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
이 문자열에는 몇 개의 단어가 있을까?
이를 구하는 프로그램을 작성하시오.

단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

"""
import sys

if __name__ == "__main__":
    sentence = sys.stdin.readline()
    delim = " \n"
    is_word = False
    cnt = 0

    for alph in sentence:
        try:
            result = delim.index(alph) # if not: Value Error
            if is_word:
                # only counts when word was true
                is_word = False
                cnt += 1
        except: # When Value Error == not in delim
            if not(is_word):
                is_word = True
    
    if is_word:
        # when the sentence ends with word, cnt++
        cnt += 1

    print(cnt)