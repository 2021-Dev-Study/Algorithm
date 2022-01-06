# 작성자: red-Pen9uin
# level 7: String
# 10809: 알파벳 찾기
"""
알파벳 소문자로만 이루어진 단어 S가 주어진다.

각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

"""
# 변수 명을 지을 때는 키워드를 잘 확인하자!
# 여러번 채점해도 틀리길래 왜인가 했더니, 변수 명을 str로 지어서 그랬던 것 같다.
import sys

if __name__ == "__main__":
    word = sys.stdin.readline()
    # strip()을 이용해 \n 문자를 제거 (검색해서 찾음)
    # 다만 여전히 len()으로 체크해봤을 때 알파벳 수보다 많은 걸 보면,
    # \n 대신 \0이 삽입되는 것 같다는 추론...
    # str = list(map(lambda s: s.strip(), str))
    
    count = [-1] * 26 # num of alphabets
    # print(len(count))
    # print(len(word))

    for i in range(0, len(word)-1):
        index = ord(word[i]) - ord('a')
        if count[index]<0 :
            count[index] = i
            # print(f"{word[i]} : {i}")
    
    for i in count :
        print(f"{i} ", end='')


"""
검색해서 찾은 답안.
python의 문자열은 find()를 제공하므로,
이런 식으로도 풀 수 있다.
"""
# if __name__ == "__main__":
#     word = sys.stdin.readline()
#     alphabet = list(range(97,123))  # 아스키코드 숫자 범위

#     for x in alphabet :
#         print(word.find(chr(x)), end=' ') 