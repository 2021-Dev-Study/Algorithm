# print(list(range(3-2)))
height, width = map(int, input().split())
mn = min(height, width) # 3

box = []
for i in range(height) :
    box.append([str(i) for i in str(input())])

# print(box)

tmp = 0
for j in range(mn-1,-1,-1) :
    # 제일 클 수 있는 정사각형 크기 ->  index제함
    # 2, 1, 0
    for i in range(height-j) : # 세로 _ 이동 가능 간격
        # j : 2 일때 -> i : 0
        # j : 1 일 때 -> i : 0, 1
        # j : 0 일 때 -> i : 0,1,2
        for k in range(width-j) : # 가로 _ 이동 가능 간격
            # j : 2 일때 -> k : 0, 1, 2
            # j : 1 일 때 -> k : 0, 1, 2, 3
            # j : 0 일 때 -> k : 0,1,2,3,4
            if box[i][k] == box[i + j][k] == box[i][k + j] ==  box[i + j][k + j]:
            # (0,0) , (2,0), (0, 2), (2,2) 등등으로 진행됨
                tmp = max(tmp, j+1) # 계산하는 index의 기준으로 값이 모두 1씩 작기 때문에 길이x길이인 결과값에 맞게 +1
print(tmp*tmp)
    # for i in range(height-j) : # range(3-3
    #     # 0
    #     # 0, 1
    #     for k in range(width-j) :
    #         # 0, 1, 2
    #
    #         if box[i][k] == box[i][k+j] == box[i+j][k] == box[i+j][k+j] :
    #             print(j)
