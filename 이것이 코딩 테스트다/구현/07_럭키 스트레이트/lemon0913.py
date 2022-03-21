if __name__ == "__main__":
    N = input()

    R = 0
    L = 0
    for i in range(len(N)):
        tmp = len(N)//2

        if i < tmp: # 왼쪽 절반은 L에 더하기
            L += int(N[i])
        else: # 오른쪽 절반은 R에 더하기
            R += int(N[i])

    # 왼쪽 절반의 합과 오른쪽 절반의 합이 같으면 'LUCKY'출력
    if R == L:
        print('LUCKY')
    else: # 아니면 'READY'출력
        print("READY")

