import sys

number: int = int(input())
storage: list = list(map(int,sys.stdin.readline().split(" ")))
print(min(storage), max(storage))