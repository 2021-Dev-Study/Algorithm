import sys
if __name__ == "__main__":
    N = int(input())
    students = [0] * N
    for i in range(N):
        students[i] = list(map(str, sys.stdin.readline().split()))
        students[i][1], students[i][2], students[i][3] = int(students[i][1]), int(students[i][2]), int(students[i][3])
    

    students.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

    for i in range(N):
        print(students[i][0])