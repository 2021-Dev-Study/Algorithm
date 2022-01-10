# 5397 : 키로거 silver_3
'''
백스페이스를 입력했다면, '-'가 주어진다. 이때, 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 
화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 
나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 
만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

<<BP<A>>Cd- [left] [right]
<           []     []
<<          []     []
<<B         [B]    []
<<BP        [B, P] []
<<BP<       [B]    [P]
<<BP<A      [B, A] [P]
<<BP<A>     [B]    [P, A]
<<BP<A>>    []     [P, A, B]
<<BP<A>>C   [C]    [P, A, B]
<<BP<A>>Cd  [C, d] [P, A, B]
<<BP<A>>Cd- [C]    [P, A, B]
'''
# 1406하고 비스무리..

n = int(input())

for i in range(n):
    left, right = [], []
    pw = input()
    
    for char in pw:
        if char == '<':
            if left:
                right.append(left.pop())
        elif char == '>':
            if right:
                left.append(right.pop())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)

    # print("".join(right[::-1] + left)) # 왜 안되는지 모르겟음..ㅠ
                                         # left  : ['B', 'A', 'P', 'C']
                                         # right : []
                                         # 머선129...왜...?

    print("".join(left + right[::-1]))