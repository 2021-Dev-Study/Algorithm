# 스택 (실버 3까지)
# 17608_막대기

import sys
if __name__ == "__main__":
    # 높이 입력받기
    N = int(input())
    heights = []
    for i in range (N):
        heights.append(int(sys.stdin.readline()))

    # reverse 배열 안의 값이 스택의 꼭대기에 저장된 값보다 크면 스택에 넣는 작업을 반복
    stack = []
    stack.append(heights.pop()) # 제일 오른쪽 값은 무조건 보이니 스택에 넣기
    for h in heights[::-1] :
        if h > stack[-1]:
            stack.append(h)      
    
    print(len(stack))

