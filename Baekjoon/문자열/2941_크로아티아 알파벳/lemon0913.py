# level 7 - 문자열
# 2941번 크로아티아 알파벳


# if __name__ == "__main__":

#     word = input()
#     count = 0

#     for i in range(len(word)):
#         if (word[i] == 'c') and (word[i+1] == '='):
#             count += 1
#             #'c='을 하나의 알파벳으로 카운트해야 하는데 for 문에 의해 '='를 따로 또 카운트하게 됨
#             # 추가로 카운트 된 것에 대해서 빼주어야 함
#             count -= 1
#             # 결과적으로 count의 값에 아무런 변화가 없음
            
#         elif (word[i] == 'c') and (word[i+1] == '-'):
#             count += 0
            
                  
#         elif (word[i] == 'd') and (word[i+1] == '-'):
#             count += 0
        
#         elif (word[i] == 'l') and (word[i+1] == 'j'):
#             count += 0
        
#         elif (word[i] == 'n') and (word[i+1] == 'j'):
#             count += 0
        
#         elif (word[i] == 's') and (word[i+1] == '='):
#             count += 0
                 
#         elif (word[i] == 'z') and (word[i+1] == '='):
#             count += 0

#         elif (word[i] == 'd') and (word[i+1] == 'z') and (word[i+2] == '='):
#             count += 1
#             #'dz='을 하나의 알파벳으로 카운트해야 하는데 for문에 의해 'z=', '='을 따로 또 카운트하게 됨
#             # 추가로 카운트 된 것에 대해서 빼주어야 함
#             count -= 1
        
#         else: #목록에 없는 문자면 알파벳 1개로 이루어잠
#             count += 1

#     print(count)

# 런타임에러(IndexError)..??????
# vscode에서는 잘 되는데??


if __name__ == "__main__":

    word = input()
    count = 0

    for i in range(len(word)):
        # i < len(word)-1 는 배열의 인덱스 범위를 벗어 발생하는 런타임에러를 막기 위해 추가
        if (i < len(word)-1 ) and (word[i] == 'c') and (word[i+1] == '='):
            count += 1
            #'c='을 하나의 알파벳으로 카운트해야 하는데 for 문에 의해 '='를 따로 또 카운트하게 됨
            # 추가로 카운트 된 것에 대해서 빼주어야 함
            count -= 1
            # 결과적으로 count의 값에 아무런 변화가 없음
            
        elif (i < len(word)-1 ) and (word[i] == 'c') and (word[i+1] == '-'):
            count += 0
            
                  
        elif (i < len(word)-1 ) and (word[i] == 'd') and (word[i+1] == '-'):
            count += 0
        
        elif (i < len(word)-1 ) and (word[i] == 'l') and (word[i+1] == 'j'):
            count += 0
        
        elif (i < len(word)-1 ) and (word[i] == 'n') and (word[i+1] == 'j'):
            count += 0
        
        elif (i < len(word)-1 ) and (word[i] == 's') and (word[i+1] == '='):
            count += 0
                 
        elif (i < len(word)-1 ) and (word[i] == 'z') and (word[i+1] == '='):
            count += 0

        elif (i < len(word)-2 ) and (word[i] == 'd') and (word[i+1] == 'z') and (word[i+2] == '='):
            count += 1
            #'dz='을 하나의 알파벳으로 카운트해야 하는데 for문에 의해 'z=', '='을 따로 또 카운트하게 됨
            # 추가로 카운트 된 것에 대해서 빼주어야 함
            count -= 1
        
        else: #목록에 없는 문자면 알파벳 1개로 이루어잠
            count += 1

    print(count)

