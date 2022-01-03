# 작성자: red-Pen9uin
# level 2: if statement
# 9498: 시험 성적
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

def main():
    score = input()
    score = int(score)

    if score<0 :
        print("Error: lower than 0")
    elif score>100 :
        print("Error: higer than 100")
    
    if (90<=score and score<=100):
        print("A")
    elif (80<=score and score<90):
        print("B")
    elif (70<=score and score<80):
        print("C")
    elif (60<=score and score<70):
        print("D")
    else:
        print("F")

if __name__ == "__main__":
	main()