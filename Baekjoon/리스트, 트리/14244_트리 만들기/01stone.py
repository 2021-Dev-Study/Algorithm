# 14244 : 트리 만들기
# 해설 봄
# 간선은 뭔지 모르겠고 그냥 ㅇㅖ제보면 순서대로 나오는듯

n, m = map(int, input().split())

for i in range(0, m-1):  # 리프
    print(i, m-1)

for i in range(m-1, n-1):
    print(i, i+1)