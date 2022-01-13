# 작성자: red-Pen9uin
# Data structure: stack
# 11899: 괄호 끼워넣기
# 수행 결과: 30864 KB / 68 ms
"""
첫 번째 줄에 올바르지 않은 괄호열 S가 주어집니다. S의 길이는 1 이상 50 이하입니다.
첫 번째 줄에 S를 올바른 괄호열으로 만들기 위해 앞과 뒤에 붙여야 할 괄호의 최소 개수를 출력합니다. 불가능한 경우는 주어지지 않습니다.

"""
import sys

def add_min_bracket(word: str) ->None:
    stack = list()
    need = list()
    cnt = -1
    
    while word:
        if word[0] == '(':
            stack.append(word[0])
            word = word[1:]
            cnt+=1

        else: # word[0] == ')':
            if (cnt<0) or stack[cnt]!='(':
                need.append(word[0])
                word = word[1:]
                
            elif stack[cnt]=='(':
                word = word[1:]
                stack.pop()
                cnt-=1

    print(f"{len(need) + len(stack)}")
    return


if __name__ == "__main__":
    word = sys.stdin.readline().rstrip('\n')
    add_min_bracket(word)