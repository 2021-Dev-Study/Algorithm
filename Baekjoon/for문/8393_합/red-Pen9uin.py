# 작성자: red-Pen9uin
# level 3: for statement
# 8393: 합
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

def main():
    num = int(input())
    sum = 0
    for i in range(1,num+1):
        sum = sum+i
    
    print(f"{sum}")
        

if __name__ == "__main__":
	main()