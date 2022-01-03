# 작성자: red-Pen9uin
# level 2: if statement
# 2884: 알람 시계
# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

def main():
    hour, min = input().split()

    hour = int(hour)
    min = int(min)

    if min<45 :
        hour -= 1
        min += 60
        if hour<0:
            hour += 24
    
    min = min - 45

    print(f"{hour} {min}")


if __name__ == "__main__":
	main()