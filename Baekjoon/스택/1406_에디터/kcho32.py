"""
한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.
a
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
"""
import sys


# 문자를 입력 받고 바로 리스트(배열)에 넣어주기 ex) "abc" -> ["a", "b", "c"]
# 커서 위치는 문자열 마지막에 위치
ch_list = list(sys.stdin.readline().rstrip())
# cursor = len(ch_list) 틀린 것에서만
number_of_command = int(sys.stdin.readline().rstrip())
command_list = []
# for i in range(number_of_command):
#     command_list = sys.stdin.readline().rstrip().split(" ")
#     if len(command_list) == 1:
#         command = command_list[0]
#     else:
#         command, ch = command_list[0], command_list[1]
    
#     if command == 'L' and cursor != 0:
#         cursor -= 1
#     elif command == 'D' and cursor != len(ch_list):
#         cursor += 1
#     elif command == 'B' and cursor != 0:
#         ch_list.pop(cursor-1)
#         cursor -= 1
#     elif command == 'P':
#         ch_list.insert(cursor, ch)
#         cursor += 1

# print("".join(ch_list))

left = ch_list.copy()
right = []

for i in range(number_of_command):
    command_list = sys.stdin.readline().rstrip().split(" ")
    if len(command_list) == 1:
        command = command_list[0]
    else:
        command, ch = command_list[0], command_list[1]

    # left에서 right로 append로 옮기면 오른쪽은 좌우 반전이 되는 점을 유의 
    if command == 'L' and len(left):
        right.append(left.pop(-1)) # 가장 뒤에 것을
    elif command == 'D' and len(right):
        left.append(right.pop()) # 가장 최신 것을 왼쪽으로 옮기기
    elif command == 'B' and len(left):
        left.pop()
    elif command == 'P':
        left.append(ch)

print("".join(left) + "".join(right[::-1]))
