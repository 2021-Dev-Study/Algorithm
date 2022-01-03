# 작성자: red-Pen9uin
# level 7: String
# 11654: 아스키 코드
"""
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때,
주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

"""
import sys

if __name__ == "__main__":
    letter = sys.stdin.readline()
    print(ord(letter[0]))
    # C/C++은 변환이 따로 필요없지만.. python은 ord()를 이용해 변환