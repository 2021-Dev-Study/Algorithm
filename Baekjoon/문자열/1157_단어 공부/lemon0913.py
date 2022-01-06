# level 7 - 문자열
# 1157번 단어 공부


# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.



if __name__ == "__main__":
    #입력을 대문자로 통일
    word = input().upper()
    
    #각 알파벳의 갯수를 세기 위한 배열
    count_alph = [0] * 26

    for i in range(len(word)):
        for k in range(26):
            #아스키코드로 65->A
            #입력받은 word의 알파벳을 차례대로 확인함
            #알파벳에 해당하는 count_alph의 값을 1 증가
            if word[i] == chr(65+k):
                count_alph[k] += 1
    
    if count_alph.count(max(count_alph)) > 1:
        print('?')
    else:
        for i in range(26):
            if count_alph[i] == max(count_alph):
                print(chr(65+i))

    


# 배열안에서 최대값을 찾으려면 max()함수 사용
# max(lst) -> lst 배열에서 최댓값을 반환

# 배열안에서 x가 몇 개 있는지 알고 싶다면 .count()함수 사용
# lst.count(x) -> lst 배열 안에서 x의 갯수를 반환
