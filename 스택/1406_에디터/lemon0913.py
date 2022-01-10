# 스택 (실버 3까지)
# 1406번 에디터



#방법1) 이렇게 하면 시간초과남 -> 스택을 사용해서 풀어보기

# import sys

# if __name__ == "__main__":
#     # 문자열, 입력할 명령어의 개수 입력받기
#     s = input()
#     M = int(input())

#     # 커서의 위치를 나타내는 변수 cur 선언
#     # 처음에 커서의 위치는 맨 끝
#     cur = len(s)

#     # M만큼 명령어 입력받기
#     for i in range(M):
#         # for문 안에서 입력받는 경우
#         # 시간초과 방지를 위해 sys.stdin.readline 사용
#         com = sys.stdin.readline()
        
#         if com[0] == "L":
#             if cur == 0:
#                 pass
#             else:
#                 cur -= 1
            
#         elif com[0] == "D":
#             if cur == len(s):
#                 pass
#             else:
#                 cur += 1
            
#         elif com[0] == "B":
#             if cur == 0:
#                 pass
#             else:
#                 s = s[:cur-1] + s[cur:]
#                 cur -= 1
            
#         else:
#             s = s[:cur] + com[2] + s[cur:]
#             cur += 1
    
#     print(s)
            

# # 문자열 내에서 삽입 및 수정이 일어날 경우 슬라이싱을 사용하는 것이 편리함
# # 반복문 안에서 입력을 받을때는 input()이 아니라 sys.stdin.readline()을 사용하기






#방법2) 스택 사용
# 커서를 기준으로, 문자열을 스택 2개에 나눠 담기
# 값을 추가하기, 삭제하기, 커서 이동하기 등 모든 동작을 append와 pop으로 해결 가능
# append(), pop()는 O(1)이고 slice(a:b)는 O(b-a)라서 시간복잡도를 훨씬 줄일 수 있음(파이썬 자료형 별 주요연산자의 시간 복잡도 : https://wayhome25.github.io/python/2017/06/14/time-complexity/)
# 또한 커서의 위치를 변경하는 과정도 생략되어 연산 간단해짐

import sys

if __name__ == "__main__":
    # 문자열, 입력할 명령어의 개수 입력받기
    # 문자열을 커서 기준으로 str_l, str_r으로 나눔. 마지막에 둘을 합쳐서 출력할 것임
    str_l = list(input())
    str_r = []
    M = int(input())

    # M만큼 명령어 입력받기
    for _ in range(M):
        # for문 안에서 입력받는 경우
        # 시간초과 방지를 위해 sys.stdin.readline 사용
        com = sys.stdin.readline()
        
        if com[0] == "L":
            if len(str_l) == 0:
                pass
            else:
                str_r.append(str_l.pop())
            
        elif com[0] == "D":
            if len(str_r) == 0:
                pass
            else:
                str_l.append(str_r.pop())
            
        elif com[0] == "B":
            if len(str_l) == 0:
                pass
            else:
                str_l.pop()
            
        else:
            str_l.append(com[2])
    
    #str_r은 str_l에서 넘겨받은 순서대로 정렬되어 있기 때문에 뒤집어서 str_l에 붙이는 과정이 필요
    print(''.join(str_l + list(reversed(str_r))))





# 저번에 pop() 사용 불가라고 하지 않았나요..???






# 시퀀스 자료형 뒤집기는 reversed(str)
# ''.join(리스트) 하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환
# 입력받은 문자열을 list()로 변환 안하니 나중에 append 연산에서 에러남

