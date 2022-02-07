import sys


number = list(map(int,sys.stdin.readline().rstrip()))
number = sorted(number, reverse=True)

sys.stdout.write("".join(map(str,number)))