n = int(input())

three_cnt = 0

def check_three(num):
    if num // 10 == 3 or num % 10 == 3:
        return True
    else:
        return False

for hour in range(0, n + 1):
    for min in range(0, 60):
        for sec in range(0, 60):
            if check_three(sec):
                three_cnt += 1
            else:
                if check_three(min):
                    three_cnt += 1
                else:
                    if check_three(hour):
                        three_cnt += 1

print(three_cnt)