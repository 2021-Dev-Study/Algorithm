# def possible(answer):
#     for x, y, stuff in answer:
#         if stuff == 0: # 기둥 
#             if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y -1, 0] in answer:
#                 continue
#             else:
#                 return False
#         elif stuff == 1:
#             if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] or ([x - 1, y, 1]
#             in answer and [x + 1, y, 1] in answer):
#                 continue
#             else:
#                 return False
#     return True

# def solution(n, build_frame):
#     answer = []
#     for frame in build_frame:
#         x, y, stuff, operate = frame
#         if operate == 0: # 삭제
#             answer.remove([x, y, stuff])
#             if not possible(answer):
#                 answer.append([x, y, stuff])
#         elif operate == 1:
#             answer.append([x, y, stuff])
#             if not possible(answer):
#                 answer.remove([x, y, stuff])
    
#     return sorted(answer)

# def possible(built_frame):
#     for x, y, a in built_frame:
#         if a == 0:
#             if y == 0 or[x-1, y, 1] in built_frame or [x, y, 1] in built_frame or [x, y -1, 0] in built_frame:
#                 continue
#             else:
#                 return False
#         elif a == 1:
#             if [x, y - 1, 0] in built_frame or [x + 1, y - 1, 0] or ([x - 1, y, 1]
#             in built_frame and [x + 1, y, 1] in built_frame):
#                 continue
#             else:
#                 return False
#     return True


# def solution(n, build_frame):
#     answer = []
#     temp_build_frame = []
#     for cmd in build_frame:
#         if cmd[3] == 1:
#             temp_build_frame.append([cmd[0], cmd[1], cmd[2]])
#             if not(possible(temp_build_frame)):
#                 temp_build_frame.remove([cmd[0], cmd[1], cmd[2]])
#             else:
#                 continue
#         elif cmd[3] == 0:
#             temp_build_frame.remove([cmd[0], cmd[1], cmd[2]])
#             if not(possible(temp_build_frame)):
#                 temp_build_frame.append([cmd[0], cmd[1], cmd[2]])
#             else:
#                 continue
    
#     answer = sorted(temp_build_frame, key=lambda x: (x[0], x[1], x[2]))
    
#     return answer

def possible(built_frame):
    for x, y, a in built_frame:
        if a == 0:
            if y == 0 or [x - 1, y, 1] in built_frame or [x, y, 1] in built_frame or [x, y - 1, 0] in built_frame:
                continue
            else:
                return False
        elif a == 1:
            if [x, y - 1, 0] in built_frame or [x + 1, y - 1, 0] in built_frame or ([x - 1, y, 1] in built_frame and [x + 1, y, 1] in built_frame):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    temp_build_frame = []
    for cmd in build_frame:
        x, y, a, b = cmd
#         if cmd[3] == 1:
#             temp_build_frame.append([cmd[0], cmd[1], cmd[2]])
#             if not possible(temp_build_frame):
#                 temp_build_frame.remove([cmd[0], cmd[1], cmd[2]])

#         elif cmd[3] == 0:
#             temp_build_frame.remove([cmd[0], cmd[1], cmd[2]])
#             if not possible(temp_build_frame):
#                 temp_build_frame.append([cmd[0], cmd[1], cmd[2]])
#             else:
#                 continue

        if b == 1:
            temp_build_frame.append([x, y, a])
            if not possible(temp_build_frame):
                temp_build_frame.remove([x, y, a])

        elif b == 0:
            temp_build_frame.remove([x, y, a])
            if not possible(temp_build_frame):
                temp_build_frame.append([x, y, a])
        
    answer = sorted(temp_build_frame)
    
    return answer




n = 5
build_frame = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, build_frame))