import sys

n = int(input())
characters = {}
answer = 0

for _ in range(n):
    flag = False
    string = sys.stdin.readline()
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            tmp = string[i+1:]
            if string[i] in tmp:
                flag = True
                break
    if not flag:
        answer += 1

print(answer)
            
