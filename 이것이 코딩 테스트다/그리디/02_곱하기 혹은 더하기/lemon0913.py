if __name__ == "__main__":
    S = input()

    result = 0
    for i in S:
        if i == '0':
            result += 0
        elif i == '1':
            result += 1
        else:
            if result == 0:
                result += int(i)
            else:
                result *= int(i)
    
    print(result)

# 0이나 1인 경우에는 더하는게 이득
# 그 외의 숫자의 경우 곱하는게 이득, 단 이전 숫자들의 합이 0인 경우에는 일단 더해 주어야함