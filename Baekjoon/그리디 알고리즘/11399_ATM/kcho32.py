import sys

num_people = int(sys.stdin.readline())
withdrawing_time = sorted(list(map(int, sys.stdin.readline().split())))
min_time = 0

for i in range(len(withdrawing_time)):
    min_time += sum(withdrawing_time[0:i+1])

print(min_time)