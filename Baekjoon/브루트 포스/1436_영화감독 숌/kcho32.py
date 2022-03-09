from itertools import filterfalse


days_left: int = int(input())
session: list = [(i+1, tuple(map(int, input().split(" ")))) for i in range(days_left)]
possible_earns: list = []
answer_list = []

def earning(session, start, days_left, result=0):
    for i in range(start+session[start], days_left+1):
        result += session[start]