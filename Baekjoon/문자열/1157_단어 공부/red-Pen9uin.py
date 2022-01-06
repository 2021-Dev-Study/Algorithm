# 작성자: red-Pen9uin
# level 7: String
# 1157: 단어 공부
"""
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

"""
import sys

if __name__ == "__main__":
    word = sys.stdin.readline()
    ALPHABET = list(range(0x41, 0x5A+1))  # 아스키코드 숫자 범위
    alphabet = list(range(0x61, 0x7A+1))  # 아스키코드 숫자 범위
    cnt = [0] * 26

    for i in range(0, 26) :
        cnt[i] += word.count(chr(ALPHABET[i]))
        cnt[i] += word.count(chr(alphabet[i]))

    if cnt.count(max(cnt)) > 1:
        print("?")
    else:
        # 복잡한 출력식이라 가독성은 별로라고 느껴짐
        print(chr(ALPHABET[cnt.index(max(cnt))]))