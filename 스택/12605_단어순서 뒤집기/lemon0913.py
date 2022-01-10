# 스택 (실버 3까지)
# 12605_단어순서 뒤집기


#스택으로 풀기
import sys

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        str = sys.stdin.readline().split()

        stack = []
        for j in str:
            stack.append(j)
        
        print(f'Case #{i+1}: ', end="")
        for i in range(len(stack)-1):
            print(stack.pop(), end=" ")
        print(stack.pop())
            

    