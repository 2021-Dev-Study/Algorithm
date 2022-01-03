# level 7 - 문자열
# 5622번 다이얼

if __name__ == "__main__":
    
    word = input()
    count = 0

    for i in range(len(word)):
        if (word[i] == "A") or (word[i] == "B") or (word[i] == "C"):
            count += 3
        elif (word[i] == "D") or (word[i] == "E") or (word[i] == "F"):
            count += 4
        elif (word[i] == "G") or (word[i] == "H") or (word[i] == "I"):
            count += 5
        elif (word[i] == "J") or (word[i] == "K") or (word[i] == "L"):
            count += 6
        elif (word[i] == "M") or (word[i] == "N") or (word[i] == "O"):
            count += 7
        elif (word[i] == "P") or (word[i] == "Q") or (word[i] == "R") or (word[i] == "S"):
            count += 8
        elif (word[i] == "T") or (word[i] == "U") or (word[i] == "V"):
            count += 9
        elif (word[i] == "W") or (word[i] == "X") or (word[i] == "Y") or (word[i] == "Z"):
            count += 10
      
    
    print(count)
