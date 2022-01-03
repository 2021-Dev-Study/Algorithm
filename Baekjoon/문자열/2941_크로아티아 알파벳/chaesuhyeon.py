alpha = input()
count = 0
Number = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

        
for n in Number:
    if n in alpha:
        count += alpha.count(n)   # 만약에 리스트 Number에 있는 단어들이 입력된 alpha에 있다면 그 개수를 카운트 해줌
print(len(alpha)-count) # 입력받은 alpha의 전체 길이에서 count를 빼주면 됨 

##################################################
# 맨 처음 생각했던 풀이.  막막해서 하나하나 다 분류해서 하려다가 더 막막해져서 윗 문제 풀이보고 위 풀이 생각해냄
#for a in len(alpha):
#    if alpha[a] == "c":
#        if alpha[a + 1] == "="
#            count +=1
#        elif alpha[a + 1] == "-":
#            count +=1
#    elif alpha[a] == "d":
#        if alpha[a+1] == "z" and alpha[a+2] ==