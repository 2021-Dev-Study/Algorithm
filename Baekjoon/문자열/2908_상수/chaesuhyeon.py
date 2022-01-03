A,B = map(str, input().split()) #두 수 입력
A = int(A[::-1]) # 문자를 뒤집어서 출력
B = int(B[::-1])
print(max(A,B))