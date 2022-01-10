# 3986 좋은 단어 silver_4
'''
단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다.
만약 선끼리 교차하지 않으면서 
각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 
그 단어는 '좋은 단어'이다. 평석이가 '좋은 단어' 개수를 세는 것을 도와주자.
'''
# 됨 : AA, BB, AABB, BBAA, ABBA, BAAB ...
# 안됨 : AB, BA, AAA, BBB, ABAB, BABA, AAAB, ABBB ...
# 짝을 지움?
# 넣을 때 앞의 값과 비교...?
# 그럼...첫번째는 무조건 넣어야 함...

n = int(input())
cnt = 0

for i in range(n):
    word = input().rstrip() 
    stk = []

    for char in word:
        if not stk:
            stk.append(char) # 첫번째던 빈스택일때는 무조건 넣음
            continue         # 넣으면 아래 코드 실행 안하고 건너뜀
            
        if char != stk[-1]:
            stk.append(char) # 바로 앞 글자하고 다르면 넣음
        else:
            stk.pop()        # 바로 앞 글자하고 같으면 앞글자도 안넣음
    
    if not stk:
        cnt += 1  # 스택이 비면 좋은 글자
print(cnt)


