# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서,
# 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면,
# ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 단어가 들어온다.
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
#
# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.
n = int(input())
grp = 0
for _ in range(n) :
    word = input()
    fail = 0
    for i in range(len(word)-1) : # 밑에 indexing에서 i+1이 있기때문에 i+1로 마지막 자릿수 조회할 때 out of range 되지 않도록
        if word[i] == word[i+1] : # 다음자릿수와 같은지 안같은지
            pass
        elif word[i] != word[i+1]: # 다음자릿수와 다른 경우
            if word[i] in word[i+1:] : # 앞으로 남은 문자 중에 현재 문자와 동일한 문자가 있으면 그룹 단어 아님
                fail = 1 # 실패했다는 표시
            else :
                pass
    if fail == 0: # 실패한 적이 없으면
        grp += 1 # 그룹단어이기 때문에 grp에 +1
print(grp)