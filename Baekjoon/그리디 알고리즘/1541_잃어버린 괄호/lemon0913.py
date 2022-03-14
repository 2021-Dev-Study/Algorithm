# 단계별 - 그리디 알고리즘
# 1541_읽어버린 괄호

if __name__ == "__main__":
    S = input().split('-') # - 기준으로 나누기
    
    # - 기준으로 나눠진 것 각각의 합을 구하기
    result = []
    for s in S:
        tmp = s.split('+') 
        x = 0
        for i in tmp:
            x += int(i)
        result.append(x)

    # 첫번째는 더하고 나머지는 뺴기
    min_sum = result[0]
    for i in range(1, len(result)):
        min_sum -= result[i]
    print(min_sum)

    
# - 기준으로 나누기 -> 이렇게 하면 가장 첫번째 값만 + 취급하고 나머지는 -하면 됨
# 50+30-49+34-56 -> [50+30, 49+34, 56]