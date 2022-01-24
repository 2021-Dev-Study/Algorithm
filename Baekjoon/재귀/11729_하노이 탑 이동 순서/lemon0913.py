# 재귀 (단계별 & 실버5)
# 11729_하노이 탑 이동 순서

def hanoi(no, x, y):
    if no > 1:
        hanoi(no-1, x, 6-x-y)
    print(f'{x} {y}')

    if no > 1:
        hanoi(no-1, 6-x-y, y)

if __name__ == "__main__":
    N = int(input())
    print(2**N-1)
    hanoi(N, 1, 3)
