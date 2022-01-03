# 작성자: red-Pen9uin
# level 7: String
# 2941: 크로아티아 알파벳
"""
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

예를 들어, ljes=njak은
크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고,
d와 ž가 분리된 것으로 보지 않는다.
lj와 nj도 마찬가지이다.
위 목록에 없는 알파벳은 한 글자씩 센다.

"""
import sys
import copy

def cnt_croatia_1(word: str) -> int:
    # 문자열을 가지고 비교하는 방식
    string = copy.deepcopy(word)
    croatian = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")
    cnt = 0
    
    for alph in croatian:
        while string.find(alph) >= 0:
            # 문자열을 하나씩 찾아 삭제하며 찾는다
            # 이 경우, 삭제된 문자열이 하나로 합쳐지며
            # "크로아티안 문자처럼 보이는" 문자들이 생기게 된다.
            cnt += 1
            string = string.replace(alph, '', 1)
    cnt += len(string)
    return cnt


def cnt_croatia_2(word: str) -> int:
    # 직접 비교하는 방식
    # "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="
    cnt2 = 0
    string = copy.deepcopy(word)
    i = 0

    while i<len(string):
        cnt2 += 1
        if i+1 < len(string):
            if string[i] == 'c':
                if string[i+1] == '=':
                    i += 1
                elif string[i+1] == '-':
                    i += 1
            elif string[i] == 'd':
                if string[i+1] == 'z':
                    if (i+2 < len(string)) and (string[i+2] == '='):
                        i += 2
                elif string[i+1] == '-':
                    i += 1
            elif string[i] == 'l':
                if string[i+1] == 'j':
                    i += 1
            elif string[i] == 'n':
                if string[i+1] == 'j':
                    i += 1
            elif string[i] == 's':
                if string[i+1] == '=':
                    i += 1
            elif string[i] == 'z':
                if string[i+1] == '=':
                    i += 1
        i += 1
    return cnt2

def cnt_croatia_3(word: str) -> int:
    # 문자열을 가지고 비교하는 방식 - 2
    string = copy.deepcopy(word)
    croatian = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")
    
    for alph in croatian:
        while string.find(alph) >= 0:
            # 문자열을 하나씩 찾아 다른 문자로 대체하며 찾는다.
            string = string.replace(alph, '*', 1)
    return len(string)

if __name__ == "__main__":
    word = sys.stdin.readline()
    word = word.rstrip("\n")
    print(cnt_croatia_2(word))